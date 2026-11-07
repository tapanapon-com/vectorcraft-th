# VectorCraft TH — Version Log

## 0.22.0-th.1 — 7 November 2026

Based on the complete [upstream v0.22.0 release](https://github.com/storytold/vectorcraft/releases/tag/v0.22.0), commit `654749c16eb20b6d3182a96defb66e11d1a9649a`.

### การเปลี่ยนแปลงจากต้นฉบับ / Upstream changes

- เลือกความละเอียดพิกัดพาธที่บันทึกในไฟล์งาน / Select saved path-coordinate precision: [upstream change](https://github.com/storytold/vectorcraft/pull/3990).
- แก้การเปิด EPS จาก Ghostscript eps2write / Open Ghostscript eps2write EPS files: [upstream change](https://github.com/storytold/vectorcraft/pull/5314).
- รักษาหมึกสีพิเศษชื่อ All/None ขณะส่งออก PDF / Preserve spot inks named All/None in PDF export: [upstream change](https://github.com/storytold/vectorcraft/pull/5250).

The release tag was merged in full. These are selected upstream highlights, credited to their original contributors; they are not new features authored by the Thai project.

### การปรับรุ่นภาษาไทย / Thai edition changes

- เพิ่มคำแปล 107 รายการ รวม 7,920 รายการ / Added 107 translations, 7,920 catalog entries total.
- รวมข้อความใหม่ 11 รายการที่สแกนพบเพิ่มเติมจากตารางภาษาอ้างอิง / Includes 11 additional source-discovered strings beyond the reference catalogs.
- คงฟอนต์สำรอง Noto Sans Thai และชุดคำแปลเดิม / Preserve bundled Thai font fallback and existing localization.
- แพ็กเกจ Mac Apple Silicon และ Windows x64 รวม CLI สำหรับ MCP / Both platform packages include the MCP CLI.
- ช่องทางตรวจอัปเดตใช้ repository รุ่นไทย / Update checks use the Thai repository.

### ผลตรวจ / Validation

The catalog validator passed with no missing keys, duplicate entries, placeholder, numeric, escape or shortcut mismatches. The complete shared gate passed all12stages with14,487tests passed and15skipped; native platform packages are being checked before publication; final results belong in [current validation](validation-0.22.0-th.1.json) and [upgrade notes](thai-upgrade-20261107.md).

Mac packages use ad-hoc signatures and are not notarized. Windows packages are unsigned. Native Windows CI checks do not claim manual testing of every Windows GUI workflow.

Thai updates are manual downloads from this repository’s Releases. The upstream automatic checker accepts stable versions only and excludes the `-th.1` release names.

## 0.21.0-th.1 — previous release

7,813 Thai entries. The previous workspace result, 13,965 passed and 15 ignored, belongs to that release only. It remains in [the historical report](validation-th.json).
