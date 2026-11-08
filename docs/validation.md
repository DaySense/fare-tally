# Validation and development

FareTally includes a standard-library Python test suite for its offline planner and ledger auditor. It covers inclusive date windows, airport combinations, open jaws, stable case IDs, revision isolation, file preservation, query caps, timezone-aware observation ordering and evidence validation.

The planner preserves approved airport-local date combinations, including a later leg with an earlier local date across the international date line. Flight chronology and hotel nights must be checked from actual zoned timestamps and reservations, not inferred by the planner.

## Run the checks

From the repository root, with Python 3.10+:

```sh
python3 -m unittest discover -s tests -v
```

There are 14 automated tests. Passing them validates these software invariants; it does not prove that an assistant will search every carrier or find the market-wide lowest fare.

To generate the fictional example in a fresh temporary directory:

```sh
fare_tally_run_dir=$(mktemp -d)
python3 skills/fare-tally/scripts/search_matrix.py plan skills/fare-tally/examples/search-space.json --out "$fare_tally_run_dir/plan.json"
```

The example produces 36 candidate queries and no fares. An audit also needs observations in a ledger; an empty or incomplete ledger intentionally returns exit code 1. See [the schema and exit codes](../skills/fare-tally/references/coverage.md).

## Behavioral checks

[Acceptance scenarios](../tests/behavior-checks.md) cover interview quality, baggage, flexible dates, midnight arrivals, hard deadlines, revised preferences, login barriers and incomplete research. Synthetic Chinese and English trials have exercised these parts of the workflow; their prices and travelers are fictional. A limited live-browser check reached a selected return fare and baggage rules, with account eligibility kept distinct from anonymous pricing.

These trials do not establish compatibility with every agent installation or booking platform. New-account login, CAPTCHA handoff, all real date/airport combinations, visas and payment-stage totals require their own evidence when relevant. A completed fare-query audit is not a traveler-eligibility certificate.

## Build release packages

```sh
python3 tools/build_release.py
```

The builder includes only an explicit source allowlist. The GitHub source ZIP contains the repository files. The skill ZIP contains `fare-tally/SKILL.md`, its linked resources and LICENSE. Private research, account sessions, screenshots, local archives and generated caches are excluded.

When changing the version, update the builder version and both README download links together. Re-run the checks and compare the uploaded release files with the locally built files before sharing the release.
