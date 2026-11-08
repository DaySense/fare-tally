# Validation scope

The FareTally rename was rechecked on 9 November 2026: all 13 tests passed, the CLI example produced 36 queries and an empty ledger left all 36 unresolved, Ruby/Psych parsed the renamed metadata, and 19 relative Markdown links resolved. The previous FareMosaic directory and release files were retained unchanged.

The release passed 13 Python standard-library tests and the fictional example through the CLI. The tests cover inclusive endpoints, earlier/later dates, independent return dates, continuity/open jaws, stable case IDs, revision isolation, non-truncating case caps, preservation of prior files, timezone-aware observation ordering, initial plan rows versus later observations, and refusal to treat teaser/failed/invalid records as resolved final queries.

The bundled skill-creator quick_validate.py was attempted but could not import PyYAML; the package index was unreachable from the shell. Consequently a successful run of that specific validator is **not claimed**. YAML parsing and basic metadata checks were instead performed using the system Ruby/Psych parser, including the skill name/description and UI invocation metadata. Relative documentation links and ZIP paths were checked. On an environment with PyYAML, the publisher can additionally run the original skill-creator validator. PyYAML and Ruby are not runtime dependencies of the shipped helper.

Reproduce from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 skills/fare-tally/scripts/search_matrix.py plan skills/fare-tally/examples/search-space.json --out /path/to/private-research/demo-plan.json
```

The fictional example contains 36 candidate queries. It makes no network calls and returns no fares. A real audit additionally needs a ledger populated from actual observations; do not manufacture evidence to obtain a complete status.

Host-level scenarios are in [behavior-checks.md](../tests/behavior-checks.md). They have not been executed against a live booking platform as part of this release. Unit tests and file validation do not prove that an agent will always interview well, search every airline, calculate a real hotel's bill correctly, or discover the market's lowest fare.

Package with `python3 tools/build_release.py`. Only the explicit source allowlist is included; real query reports, browser sessions and the creator's earlier travel files are outside the package. Repository and single-skill ZIPs have different layouts for their respective upload/install workflows.

The v0.1.1 update changes the Chinese display name to 航价笔记 and adds its separate screening record. Earlier name research and v0.1.0 ZIPs are retained; the research helper is unchanged.
