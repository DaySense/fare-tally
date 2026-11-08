#!/usr/bin/env python3
"""Build clean source and single-skill ZIPs from an explicit file allowlist."""
from pathlib import Path
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'dist'
VERSION = '0.1.3'
FILES = [
    '.gitignore', 'LICENSE', 'README.md', 'README.zh-CN.md',
    'docs/validation.md',
    'skills/fare-tally/SKILL.md', 'skills/fare-tally/agents/openai.yaml',
    'skills/fare-tally/references/intake.md',
    'skills/fare-tally/references/search-and-evidence.md',
    'skills/fare-tally/references/results.md',
    'skills/fare-tally/references/coverage.md',
    'skills/fare-tally/scripts/search_matrix.py',
    'skills/fare-tally/examples/search-space.json',
    'tests/test_search_matrix.py', 'tests/behavior-checks.md', 'tools/build_release.py'
]


def main():
    for item in FILES:
        p = ROOT / item
        if not p.is_file() or p.is_symlink(): raise SystemExit(f'Missing or unsafe source: {item}')
    OUTPUT.mkdir(exist_ok=True)
    source = OUTPUT/f'fare-tally-github-v{VERSION}.zip'
    skill = OUTPUT/f'fare-tally-skill-v{VERSION}.zip'
    with zipfile.ZipFile(source, 'w', zipfile.ZIP_DEFLATED) as z:
        for item in FILES: z.write(ROOT/item, 'fare-tally/'+item)
    with zipfile.ZipFile(skill, 'w', zipfile.ZIP_DEFLATED) as z:
        for item in FILES:
            prefix = 'skills/fare-tally/'
            if item.startswith(prefix): z.write(ROOT/item, 'fare-tally/'+item[len(prefix):])
        z.write(ROOT/'LICENSE', 'fare-tally/LICENSE')
    print(json.dumps({'source_zip': str(source), 'skill_zip': str(skill), 'source_files': len(FILES)}, indent=2))


if __name__ == '__main__': main()
