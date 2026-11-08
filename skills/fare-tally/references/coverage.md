# Offline search matrix

Python 3.10+, standard library only. This tool never accesses a network, reads browser sessions, quotes fares or books anything. Run it from the skill directory. Put private plans/ledgers outside the public repository.

## Input

See [the fictional example](../examples/search-space.json). Fields:

- `version`: 1; `revision`: a nonempty constraint revision, e.g. `r1`.
- `families`: every approved itinerary family, each with unique `id`, `allow_open_jaw` and ordered `segments`.
- Each segment: unique `id`, approved three-letter `origins`/`destinations`, and `dates` as a list or inclusive `{start,end}`. Both endpoints are included; inputs are deduplicated and sorted.
- `allow_open_jaw: false` requires each leg's origin to equal the previous destination. `true` permits approved ground gaps and records them, without implying that they are free/feasible. Use separate families or narrower airport sets if only specific gaps are approved.

Do not encode preferences the user did not accept. The only automatic filters are same-origin/destination removal, nondecreasing departure dates and the specified continuity rule. Same-day onward departures remain candidates until actual flight times are known.

**Departure-day differences are not hotel-night counts.** For multi-city stays, derive sufficiently broad departure domains from the agreed range and possible arrival patterns; then assess nights, deadlines and usable days from actual selected flights. The generator does not validate time-of-day, route existence, visas or price.

## Commands

```bash
python3 scripts/search_matrix.py plan examples/search-space.json --out /path/to/private-research/plan.json
python3 scripts/search_matrix.py audit /path/to/private-research/plan.json /path/to/private-research/ledger.json --out /path/to/private-research/audit.json
```

Default cap: 10,000 cases. Exceeding it is an error, **not a truncated plan**; no new output plan is written. Explicitly narrow/partition the agreed scope or raise `--max-cases`. Existing outputs are not overwritten unless `--replace` is supplied; prefer a new file per revision.

Copy stable case IDs from the plan to the [ledger](results.md). Audit uses current-revision observations, selecting the latest timestamp. Initial `planned` rows may be undated and do not override dated observations. Actual attempts/observations need a timezone-aware timestamp and source; invalid current-revision entries prevent that case from appearing resolved until corrected. Conflicting observations at the same timestamp are flagged. Stale/unknown case entries are reported, never counted as current evidence.

Audit gives family and leg/airport/date coverage, pending IDs and invalid entries. Exit codes: 0 = plan generated or all queries resolved; 1 = audit gaps/errors/unknown cases; 2 = invalid input, case cap or file error. Query coverage is not proof that every timing/carrier has been inspected, nor a cheapest-fare certificate.
