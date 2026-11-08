#!/usr/bin/env python3
"""Offline candidate-query planner and coverage auditor; never fetches fares."""
import argparse
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import sys

STATES = {"planned", "stage_price", "checked_final", "no_results", "infeasible",
          "loading_failed", "blocked", "skipped"}
TERMINAL = {"checked_final", "no_results", "infeasible"}


def day(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Dates must be explicit YYYY-MM-DD strings")
    return date.fromisoformat(value)


def dates(value):
    if isinstance(value, list) and value:
        return sorted({day(v).isoformat() for v in value})
    if isinstance(value, dict) and set(value) == {"start", "end"}:
        start, end = day(value["start"]), day(value["end"])
        length = (end - start).days + 1
        if not 1 <= length <= 3660:
            raise ValueError("Date range must be ordered and at most 3660 inclusive days")
        return [(start + timedelta(days=i)).isoformat() for i in range(length)]
    raise ValueError("dates must be a nonempty list or inclusive {start,end}")


def codes(value):
    if not isinstance(value, list) or not value:
        raise ValueError("Airport/city code lists must not be empty")
    result = set()
    for v in value:
        if not isinstance(v, str) or not re.fullmatch(r"[A-Za-z]{3}", v):
            raise ValueError("Use approved three-letter airport/city codes")
        result.add(v.upper())
    return sorted(result)


def normalize(spec):
    if not isinstance(spec, dict) or type(spec.get("version")) is not int or spec.get("version") != 1 or not isinstance(spec.get("revision"), str) or not spec["revision"].strip():
        raise ValueError("version=1 and a nonempty constraint revision are required")
    families = spec.get("families")
    if not isinstance(families, list) or not families:
        raise ValueError("At least one route family is required")
    clean = {"version": 1, "revision": spec["revision"], "families": []}
    family_ids = set()
    for f in families:
        if not isinstance(f, dict):
            raise ValueError("Each route family must be an object")
        fid = f.get("id")
        if not isinstance(fid, str) or not re.fullmatch(r"[a-zA-Z0-9_-]+", fid) or fid in family_ids:
            raise ValueError("Family IDs must be unique ASCII slugs")
        family_ids.add(fid)
        gap = f.get("allow_open_jaw", False)
        if not isinstance(gap, bool):
            raise ValueError("allow_open_jaw must be true or false")
        segments = f.get("segments")
        if not isinstance(segments, list) or not segments:
            raise ValueError("Each family needs ordered segments")
        nf = {"id": fid, "allow_open_jaw": gap, "segments": []}
        segment_ids = set()
        for s in segments:
            if not isinstance(s, dict):
                raise ValueError("Each segment must be an object")
            sid = s.get("id")
            if not isinstance(sid, str) or not re.fullmatch(r"[a-zA-Z0-9_-]+", sid) or sid in segment_ids:
                raise ValueError("Segment IDs must be unique slugs within a family")
            segment_ids.add(sid)
            nf["segments"].append({"id": sid, "origins": codes(s.get("origins")),
                                   "destinations": codes(s.get("destinations")),
                                   "dates": dates(s.get("dates"))})
        clean["families"].append(nf)
    clean["families"].sort(key=lambda f: f["id"])
    return clean


def generate(spec, max_cases=10000):
    """Keep every approved local-date combination; defer chronology to zoned times."""
    if isinstance(max_cases, bool) or max_cases < 1:
        raise ValueError("max_cases must be positive")
    clean = normalize(spec)
    cases = []
    for family in clean["families"]:
        def walk(index, chosen):
            if index == len(family["segments"]):
                key = json.dumps([family["id"], chosen], sort_keys=True, separators=(",", ":"))
                cid = family["id"] + "-" + hashlib.sha256(key.encode()).hexdigest()[:16]
                gaps = [{"after_segment": a["id"], "from": a["destination"], "to": b["origin"]}
                        for a, b in zip(chosen, chosen[1:]) if a["destination"] != b["origin"]]
                cases.append({"case_id": cid, "family_id": family["id"],
                              "legs": list(chosen), "ground_gaps": gaps})
                if len(cases) > max_cases:
                    raise ValueError(f"More than {max_cases} candidate queries; no truncated plan was written. "
                                     "Agree narrower domains, split explicit families, or raise --max-cases.")
                return
            s = family["segments"][index]
            for origin, destination, d in itertools.product(s["origins"], s["destinations"], s["dates"]):
                if origin == destination:
                    continue
                # Local calendar dates at different airports cannot establish chronology.
                # A westbound date-line crossing can make a later leg depart "yesterday".
                if chosen and not family["allow_open_jaw"] and origin != chosen[-1]["destination"]:
                    continue
                walk(index + 1, chosen + [{"id": s["id"], "origin": origin,
                                         "destination": destination, "date": d}])
        walk(0, [])
    if not cases:
        raise ValueError("No continuous candidate queries; review the agreed airport domains")
    digest = hashlib.sha256(json.dumps(clean, sort_keys=True).encode()).hexdigest()
    return {"version": 1, "planner_revision": "local-date-preserving-v2",
            "revision": clean["revision"], "space_sha256": digest,
            "scope": clean, "case_count": len(cases), "cases": cases,
            "limits": "Departure-date queries only. No live fares, timing coverage, arrival/stay validation or global-minimum certification."}


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("checked_at needs a timezone-aware ISO timestamp")
    t = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if t.tzinfo is None or t.utcoffset() is None:
        raise ValueError("checked_at must include a timezone offset")
    return t.astimezone(timezone.utc)


def validate_entry(e):
    state = e.get("status")
    if state not in STATES:
        raise ValueError("Unknown ledger status")
    t = timestamp(e["checked_at"]) if e.get("checked_at") else None
    if state != "planned":
        if t is None or not isinstance(e.get("source"), str) or not e["source"].strip():
            raise ValueError("Observed/attempted queries need checked_at and source")
        if state == "infeasible" and (not isinstance(e.get("reason"), str) or not e["reason"].strip()):
            raise ValueError("infeasible requires a reason, not just an invalid cheapest flight")
    if state == "checked_final":
        amount = e.get("amount")
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or not math.isfinite(amount) or amount < 0:
            raise ValueError("A final quote needs a finite nonnegative numeric amount")
        if not re.fullmatch(r"[A-Z]{3}", str(e.get("currency", ""))):
            raise ValueError("A final quote needs a three-letter currency")
        if e.get("evidence_level") not in {"final_itinerary_list", "prepayment_total"}:
            raise ValueError("A teaser/selection-stage quote is not final evidence")
        if e.get("party_basis") not in {"per_person", "entire_party"}:
            raise ValueError("A final quote needs a party_basis")
    return t


def audit(plan, ledger):
    cases = plan.get("cases", [])
    if not cases or len({c["case_id"] for c in cases}) != len(cases):
        raise ValueError("Plan must contain nonempty, unique case IDs")
    known = {c["case_id"] for c in cases}
    entries = ledger.get("entries") if isinstance(ledger, dict) else ledger
    if not isinstance(entries, list):
        raise ValueError("Ledger must be a list or {entries: [...]} object")
    latest, invalid_cases = {}, set()
    errors, stale, unknown = [], [], []
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            errors.append({"entry": i, "error": "Entry must be an object"}); continue
        cid = e.get("case_id")
        if cid not in known:
            unknown.append({"entry": i, "case_id": cid}); continue
        if e.get("revision") != plan.get("revision"):
            stale.append({"entry": i, "case_id": cid}); continue
        try:
            t = validate_entry(e)
        except (ValueError, TypeError) as exc:
            invalid_cases.add(cid); errors.append({"entry": i, "case_id": cid, "error": str(exc)}); continue
        # Undated initial plan rows must not override later real observations.
        key = t or datetime.min.replace(tzinfo=timezone.utc)
        if cid in latest and key == latest[cid][0] and e != latest[cid][1]:
            invalid_cases.add(cid); errors.append({"entry": i, "case_id": cid, "error": "Conflicting observations at the same time"})
        if cid not in latest or key >= latest[cid][0]:
            latest[cid] = (key, e)
    resolved, pending = [], []
    families = defaultdict(lambda: Counter(total=0, resolved=0, pending=0))
    axes = defaultdict(lambda: Counter(total=0, resolved=0, pending=0))
    states = Counter()
    for c in cases:
        cid = c["case_id"]
        state = latest[cid][1]["status"] if cid in latest else "planned"
        done = cid not in invalid_cases and state in TERMINAL
        (resolved if done else pending).append(cid)
        states["invalid" if cid in invalid_cases else state] += 1
        groups = [families[c["family_id"]]]
        groups += [axes[f'{c["family_id"]}/{l["id"]}/{l["origin"]}-{l["destination"]}/{l["date"]}'] for l in c["legs"]]
        for group in groups:
            group["total"] += 1; group["resolved" if done else "pending"] += 1
    return {"revision": plan["revision"], "planned_queries": len(cases),
            "resolved_queries": len(resolved), "pending_queries": len(pending),
            "all_queries_resolved": not pending and not errors and not unknown,
            "states": dict(states), "by_family": dict(families), "by_leg_airport_date": dict(axes),
            "pending_case_ids": pending, "invalid_entries": errors,
            "stale_entries": stale, "unknown_case_entries": unknown,
            "limits": "Query coverage only; not proof of traveler eligibility, truth, every flight/carrier/time inspected, availability, or a global minimum."}


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, payload, replace=False):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w" if replace else "x", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write("\n")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    build = sub.add_parser("plan")
    build.add_argument("spec"); build.add_argument("--out", required=True)
    build.add_argument("--max-cases", type=int, default=10000)
    build.add_argument("--replace", action="store_true")
    check = sub.add_parser("audit")
    check.add_argument("plan"); check.add_argument("ledger")
    check.add_argument("--out"); check.add_argument("--replace", action="store_true")
    args = p.parse_args(argv)
    try:
        if args.command == "plan":
            result = generate(read(args.spec), args.max_cases)
            save(args.out, result, args.replace)
            print(json.dumps({"revision": result["revision"], "case_count": result["case_count"],
                              "out": args.out, "note": result["limits"]}, ensure_ascii=False))
            return 0
        result = audit(read(args.plan), read(args.ledger))
        if args.out:
            save(args.out, result, args.replace)
        compact = {k: result[k] for k in ["revision", "planned_queries", "resolved_queries", "pending_queries", "all_queries_resolved", "by_family"]}
        compact.update(invalid_entries=len(result["invalid_entries"]), stale_entries=len(result["stale_entries"]),
                       unknown_case_entries=len(result["unknown_case_entries"]), next_case_ids=result["pending_case_ids"][:10], limits=result["limits"])
        print(json.dumps(compact, ensure_ascii=False, indent=2))
        return 0 if result["all_queries_resolved"] else 1
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
