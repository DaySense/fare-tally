import copy
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/fare-tally/scripts/search_matrix.py'
spec = importlib.util.spec_from_file_location('search_matrix', SCRIPT)
matrix = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix)


def space(open_jaw=False):
    return {'version': 1, 'revision': 'r1', 'families': [{
        'id': 'trip', 'allow_open_jaw': open_jaw, 'segments': [
            {'id': 'out', 'origins': ['AAA'], 'destinations': ['BBB', 'CCC'],
             'dates': {'start': '2028-05-01', 'end': '2028-05-03'}},
            {'id': 'back', 'origins': ['BBB', 'CCC'], 'destinations': ['AAA'],
             'dates': ['2028-05-02', '2028-05-03', '2028-05-04']}
        ]}]}


def final(case_id, **changes):
    e = dict(case_id=case_id, revision='r1', status='checked_final',
             checked_at='2028-04-01T12:00:00+08:00', source='fictional-test',
             amount=400, currency='SGD', party_basis='entire_party',
             evidence_level='final_itinerary_list')
    e.update(changes)
    return e


class MatrixTests(unittest.TestCase):
    def test_complete_grid_matches_independent_oracle(self):
        plan = matrix.generate(space())
        got = {(c['legs'][0]['destination'], c['legs'][0]['date'], c['legs'][1]['date']) for c in plan['cases']}
        expected = {(airport, f'2028-05-0{a}', f'2028-05-0{b}')
                    for airport, a, b in itertools.product(['BBB', 'CCC'], [1, 2, 3], [2, 3, 4]) if b >= a}
        self.assertEqual(got, expected)
        self.assertIn(('BBB', '2028-05-01', '2028-05-04'), got)
        self.assertIn(('CCC', '2028-05-03', '2028-05-03'), got)

    def test_open_jaws_are_explicit_and_not_free(self):
        strict = matrix.generate(space(False))
        flexible = matrix.generate(space(True))
        self.assertEqual(len(flexible['cases']), 2 * len(strict['cases']))
        self.assertTrue(all(not c['ground_gaps'] for c in strict['cases']))
        self.assertTrue(any(c['ground_gaps'] for c in flexible['cases']))

    def test_stable_ids_survive_input_reordering(self):
        a = space(); b = copy.deepcopy(a)
        b['families'][0]['segments'][0]['destinations'].reverse()
        b['families'][0]['segments'][1]['dates'].reverse()
        self.assertEqual(matrix.generate(a)['cases'], matrix.generate(b)['cases'])

    def test_revision_changes_do_not_reuse_old_evidence(self):
        p = matrix.generate(space()); q = copy.deepcopy(p); q['revision'] = 'r2'
        result = matrix.audit(q, [final(c['case_id']) for c in p['cases']])
        self.assertEqual(result['resolved_queries'], 0)
        self.assertEqual(len(result['stale_entries']), p['case_count'])

    def test_cap_never_writes_a_truncated_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp)/'input.json', Path(tmp)/'plan.json'
            source.write_text(json.dumps(space()))
            run = subprocess.run([sys.executable, str(SCRIPT), 'plan', str(source), '--max-cases', '1', '--out', str(target)], capture_output=True)
            self.assertEqual(run.returncode, 2)
            self.assertFalse(target.exists())

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)/'existing.json'; target.write_text('earlier result')
            with self.assertRaises(FileExistsError): matrix.save(target, {'x': 1})
            self.assertEqual(target.read_text(), 'earlier result')

    def test_stage_and_loading_failure_are_not_resolved(self):
        p = matrix.generate(space()); cid = p['cases'][0]['case_id']
        for state in ['stage_price', 'loading_failed', 'blocked', 'skipped', 'planned']:
            report = matrix.audit(p, [final(cid, status=state)])
            self.assertEqual(report['resolved_queries'], 0)
            self.assertFalse(report['all_queries_resolved'])

    def test_final_needs_currency_party_and_final_evidence(self):
        p = matrix.generate(space()); cid = p['cases'][0]['case_id']
        for change in [dict(amount=True), dict(amount=float('nan')), dict(amount=-1),
                       dict(currency=''), dict(evidence_level='teaser'), dict(party_basis='')]:
            report = matrix.audit(p, [final(cid, **change)])
            self.assertEqual(report['resolved_queries'], 0)
            self.assertEqual(len(report['invalid_entries']), 1)

    def test_aware_time_ordering_and_new_failure_remain_pending(self):
        p = matrix.generate(space()); cid = p['cases'][0]['case_id']
        # 05:00Z is later than 12:00+08:00 (04:00Z), despite clock strings.
        report = matrix.audit(p, [final(cid), final(cid, status='loading_failed', checked_at='2028-04-01T05:00:00Z')])
        self.assertEqual(report['resolved_queries'], 0)

    def test_complete_queries_still_carry_market_limit(self):
        p = matrix.generate(space())
        report = matrix.audit(p, [final(c['case_id']) for c in p['cases']])
        self.assertTrue(report['all_queries_resolved'])
        self.assertEqual(report['resolved_queries'], p['case_count'])
        self.assertIn('global minimum', report['limits'])

    def test_initial_plan_row_does_not_override_later_final(self):
        p = matrix.generate(space()); cid = p['cases'][0]['case_id']
        r = matrix.audit(p, [dict(case_id=cid, revision='r1', status='planned'), final(cid)])
        self.assertEqual(r['resolved_queries'], 1)
        r = matrix.audit(p, [final(cid), dict(case_id=cid, revision='r1', status='loading_failed')])
        self.assertEqual(r['resolved_queries'], 0)
        self.assertTrue(r['invalid_entries'])

    def test_conflicts_and_invalid_current_entries_do_not_hide(self):
        p = matrix.generate(space()); cid = p['cases'][0]['case_id']
        r = matrix.audit(p, [final(cid), final(cid, amount=399)])
        self.assertEqual(r['resolved_queries'], 0)
        self.assertTrue(r['invalid_entries'])

    def test_reversed_range_and_naive_time_rejected(self):
        bad = space(); bad['families'][0]['segments'][0]['dates'] = {'start': '2028-05-03', 'end': '2028-05-01'}
        with self.assertRaises(ValueError): matrix.generate(bad)
        p = matrix.generate(space())
        r = matrix.audit(p, [final(p['cases'][0]['case_id'], checked_at='2028-04-01T12:00:00')])
        self.assertTrue(r['invalid_entries'])


if __name__ == '__main__': unittest.main()
