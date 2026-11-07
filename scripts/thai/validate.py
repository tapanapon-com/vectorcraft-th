#!/usr/bin/env python3
"""Validate Thai catalog syntax, placeholders, numbers and source-catalog coverage."""
from pathlib import Path
from collections import Counter
import re,json

ROOT = Path(__file__).resolve().parents[2]
CATALOGS = ROOT / 'crates/ui-egui/src/i18n'

def read(path):
    rows = {}
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line or line.startswith('#'):
            continue
        fields = line.split('\t')
        if len(fields) != 3:
            raise ValueError(f'{path.name}:{n}: expected three TSV fields')
        ctx, source, target = fields
        if (ctx, source) in rows:
            raise ValueError(f'{path.name}:{n}: duplicate key {source!r}')
        rows[ctx, source] = target
    return rows

def placeholders(text):
    return Counter(re.findall(r'\{[^{}]*\}', text))

def numbers(text):
    # Ignore digits in placeholder identifiers, but preserve numeric UI values.
    return Counter(re.findall(r'\d+(?:\.\d+)?', re.sub(r'\{[^{}]*\}', '', text)))

def validate():
    thai = read(CATALOGS / 'th.tsv')
    expected = set()
    for path in CATALOGS.glob('*.tsv'):
        if path.stem != 'th':
            expected.update(read(path))
    expected.update(map(tuple,json.loads(Path(__file__).with_name("source-keys.json").read_text(encoding="utf-8"))))
    errors = []
    for (ctx, source), target in thai.items():
        comparison = source.split('|')[-1] if ctx in ('@plural', '@msgplural') else source
        if not target.strip():
            errors.append(f'Empty translation: {source}')
        if placeholders(comparison) != placeholders(target):
            errors.append(f'Placeholders: {source} => {target}')
        if ctx != '@id' and numbers(comparison) != numbers(target):
            errors.append(f'Numbers: {source} => {target}')
        if Counter(re.findall(r'\\[nt]', comparison)) != Counter(re.findall(r'\\[nt]', target)):
            errors.append(f'Escapes: {source} => {target}')
        if Counter(re.findall('[⌘⌥⇧↩↵←→]', comparison)) != Counter(re.findall('[⌘⌥⇧↩↵←→]', target)):
            errors.append(f'Shortcut symbols: {source} => {target}')
        if not ctx and source.endswith('…') != target.endswith('…'):
            errors.append(f'Ellipsis: {source} => {target}')
        if ctx in ('@plural', '@msgplural') and '|' in target:
            errors.append(f'Thai must have one plural form: {source}')
    missing = expected - thai.keys()
    for key in sorted(missing):
        errors.append(f'Missing: {key}')
    print(f'{len(thai)} Thai entries; {len(expected)} reference/source keys; {len(errors)} errors')
    for error in errors:
        print(error)
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(validate())
