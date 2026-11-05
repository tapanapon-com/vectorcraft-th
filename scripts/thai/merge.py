#!/usr/bin/env python3
"""Merge a local draft with shared seeds and reviewed terminology. No model dependency."""
import json,re,sys
from pathlib import Path
from validate import CATALOGS,read
p=CATALOGS/'th.tsv';rows=read(p)
for line in Path(sys.argv[1]).read_text().splitlines():
 d=json.loads(line);rows[tuple(d['key'])]=d['translation']
terms={
 'area type':{'ประเภทพื้นที่':'ข้อความแบบพื้นที่','รูปแบบพื้นที่':'ข้อความแบบพื้นที่'},
 'type on a path':{'ประเภทบนพาธ':'ข้อความบนพาธ','ประเภทของพาธ':'ข้อความบนพาธ'},
 'point type':{'ชนิดจุด':'ข้อความแบบจุด'},
 'lock':{'ล็ก':'ล็อก'},
 'arrowhead':{'หัวพิมพ์':'หัวลูกศร'},
 'widget':{'วิชั่น':'ตัวปรับ'},
 'color guide':{'เส้นทางสี':'คู่มือสี'},
 'metadata':{'ข้อมูลร่วมกัน':'ข้อมูลเมตา'},
 'perspective':{'กริดมิติ':'กริดทัศนมิติ','กริดมุมมอง':'กริดทัศนมิติ'},
 'raster':{'เรซิสต์':'ราสเตอร์','ราสเตอร์์':'ราสเตอร์'},
 'effect':{'ผลลัพธ์':'เอฟเฟกต์'},
 'clipboard':{'บัตรตัดต่อ':'คลิปบอร์ด'},
 'bleed':{'รั่วไหล':'ระยะตัดตก'},
 'dialog':{'ช่องโต้ตอบ':'กล่องโต้ตอบ'},
 'library':{'ห้องสมุด':'คลัง','ห้องเก็บ':'คลัง'},
 'gradient mesh':{'กริดมีชีส':'ตาข่ายไล่ระดับสี','กราดิเอนต์เน็ตเวิร์ก':'ตาข่ายไล่ระดับสี'},
 'gradient':{'กราดเส้นตรง':'ไล่ระดับสีเชิงเส้น','กราดิเอนต์':'ไล่ระดับสี','กรัเดียนต์':'ไล่ระดับสี','กรัดเอนท์':'ไล่ระดับสี'},
 'asset':{'ทรัพย์สิน':'แอสเซ็ต'},
 'artboard':{'อาร์ตบอรด':'อาร์ตบอร์ด'},
 'path':{'เส้นทาง':'พาธ'},
 'anchor':{'จุดติดตั้ง':'จุดยึด','จุดยึดหลัก':'จุดยึด'},
 'panel':{'ป้าย':'แผง'},
 'leading':{'การนำ':'ระยะบรรทัด','ความนำ':'ระยะบรรทัด'},
 'tracking':{'การติดตาม':'ระยะห่างตัวอักษร'},
 'noise':{'เสียงรบกวน':'นอยส์'},
 'pressure':{'ความดัน':'แรงกด'},
}
for k,tr in list(rows.items()):
 tr=tr.replace('ต้องเป็นtrue','ต้องเป็น true')
 for number in re.findall(r'\b\d{1,3}(?:,\d{3})+\b',tr):
  if number not in k[1] and number.replace(',','') in k[1]:tr=tr.replace(number,number.replace(',',''))
 if k[1].startswith('Export') and tr.startswith('ส่ง') and not tr.startswith('ส่งออก'):tr='ส่งออก'+tr[3:]
 if k[1].startswith('Exporting') and tr.startswith('กำลังส่ง') and not tr.startswith('กำลังส่งออก'):tr=tr.replace('กำลังส่ง','กำลังส่งออก',1)
 for term,replacements in terms.items():
  if term in k[1].lower():
   for old,new in replacements.items():tr=tr.replace(old,new)
 # Error diagnostics must retain literal parameter names and code examples.
 if k[0] == '@msg':
  missing=[token for token in re.findall(r'`[^`]+`',k[1]) if token not in tr and '{' not in token]
  if missing:tr=' / '.join(dict.fromkeys(missing))+': '+tr
  code_names=re.findall(r'\b[a-z][a-zA-Z]+\.[a-zA-Z][a-zA-Z.]+\b',k[1])
  missing_code=[name for name in code_names if name not in tr]
  if missing_code:tr=' / '.join(dict.fromkeys(missing_code))+': '+tr
  if ' pt' in k[1] and ' pt' not in tr:tr=tr.replace(' หน่วย',' pt')
 # A source's terminal ellipsis remains terminal after localization.
 if not k[0]:tr=tr.rstrip('…')+('…' if k[1].endswith('…') else '')
 if not k[0]:
  leading=re.match(r'^\s*',k[1]).group()
  trailing=re.search(r'\s*$',k[1]).group()
  tr=leading+tr.strip()+trailing
 rows[k]=tr
for k,v in read(Path(__file__).with_name('overrides.tsv')).items():
 if k in rows:rows[k]=v
header='# Thai localization for VectorCraft (MIT OR Apache-2.0).\n# Machine-assisted draft with terminology review; see docs/localization-th.md.\n# Context<TAB>English source<TAB>Thai translation.\n'
temporary=p.with_suffix('.tmp')
temporary.write_text(header+''.join('\t'.join((*k,v))+'\n' for k,v in sorted(rows.items())))
temporary.replace(p)
print(f'{len(rows)} Thai entries')
