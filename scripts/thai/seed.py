#!/usr/bin/env python3
"""Seed Thai wording from the MIT/Apache sibling catalogs; keep technical constants."""
from pathlib import Path
import argparse,json,re
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'crates/ui-egui/src/i18n'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--overwrite',action='store_true',help='replace an existing Thai catalog with an initial seed')
if (D/'th.tsv').exists() and not parser.parse_args().overwrite:
 raise SystemExit('Thai catalog already exists; use --overwrite only when intentionally reseeding.')
def read(p):
 rows={}
 for l in p.read_text().splitlines():
  a=l.split('\t')
  if len(a)==3 and not l.startswith('#'):rows[tuple(a[:2])]=a[2]
 return rows
refs=defaultdict(list)
for p in D.glob('*.tsv'):
 if p.stem!='th':
  for k,v in read(p).items():refs[k].append(v)
shared={};plain={}
for p in [ROOT.parent/'craft-i18n/locales/th/common.tsv', ROOT.parent/'craft-i18n/locales/th/pdfcraft.tsv',ROOT.parent/'filmcraft/crates/ui-egui/src/i18n/th.tsv',ROOT.parent/'photocraft/crates/ui-egui/src/i18n/th.tsv']:
 for k,v in read(p).items():
  shared[k]=v
  if not k[0]:plain[k[1]]=v
rows={}
for k,values in refs.items():
 ctx,s=k
 if k in shared:rows[k]=shared[k]
 elif ctx in ('','@msg') and s in plain:rows[k]=plain[s]
 elif len(s)<46 and all(v==s for v in values) and len(values)>=10:rows[k]=s
rows['@id','file.close']='ปิด'
rows['@id','pathfinder.add']='รวมรูปทรง'
header='# Thai localization for VectorCraft (MIT OR Apache-2.0).\n# Context<TAB>English source<TAB>Thai translation.\n'
(D/'th.tsv').write_text(header+''.join('\t'.join((*k,v))+'\n' for k,v in sorted(rows.items())))
Path('/tmp/vectorcraft-keys.json').write_text(json.dumps(sorted(refs),ensure_ascii=False))
print(f'{len(rows)} seeded / {len(refs)} reference keys; {len(refs)-len(rows)} left to translate')
