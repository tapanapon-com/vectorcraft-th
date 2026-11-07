# VectorCraft ภาษาไทย / Thai localization

รุ่นภาษาไทยนี้ต่อยอดจาก [VectorCraft โดย storytold](https://github.com/storytold/vectorcraft) รุ่น 0.22.0 ที่ commit `654749c16eb20b6d3182a96defb66e11d1a9649a` เป็นงานแปลอิสระ ไม่ใช่รุ่นทางการหรือรุ่นที่ได้รับการรับรองจากต้นฉบับ

## การทำงานและการเลือกภาษา

VectorCraft เป็นแอปวาดภาพเวกเตอร์แบบเนทีฟ เขียนด้วย Rust และใช้ egui/wgpu สำหรับหน้าจอ งานประกอบด้วยพาธ จุดยึด รูปทรง ตัวอักษร เลเยอร์ และอาร์ตบอร์ด คำสั่งจากหน้าจอ CLI และระบบควบคุมอัตโนมัติเรียกใช้เอนจินเดียวกัน

เลือกภาษาไทยจาก Preferences › User Interface › Language › ไทย (การตั้งค่า › ส่วนติดต่อผู้ใช้ › ภาษา) หรือคำสั่ง `prefs.set` ที่กำหนด `interfaceLanguage` เป็น `th` ระบบรู้จักรหัสภูมิภาค `th-TH` ด้วย หน้าจอผูก Noto Sans Thai ที่แนบมาเป็นฟอนต์สำรองสำหรับทุกตระกูลฟอนต์ UI จึงไม่ต้องอาศัยฟอนต์ไทยที่ติดตั้งในเครื่อง คำแปลฝังในแอปและทำงานออฟไลน์ โดยไม่แปลชื่อไฟล์ เนื้อหาเอกสาร และรหัสคำสั่งของผู้ใช้

ตารางภาษาอยู่ใน `crates/ui-egui/src/i18n/th.tsv` ใช้หนึ่งรูปสำหรับจำนวนทุกค่า รวมทั้งข้อความสถานะที่มีจำนวน (`@msgplural`) คำแปลเริ่มจากข้อความร่วมของ FilmCraft, PhotoCraft และ craft-i18n รวมกับร่างที่ช่วยแปลด้วยโมเดลภาษาในเครื่อง แล้วปรับคำศัพท์และตรวจรูปแบบ ไม่ได้คัดลอกทรัพยากรจาก Adobe หรือแอปปิดซอร์ส

## ความครอบคลุมของคำแปล

ตารางภาษาไทยมี 7,920 รายการ ครอบคลุมคีย์ในแค็ตตาล็อกอ้างอิงและรายการเพิ่มเติมที่สแกนจากซอร์สของรุ่นนี้ การตรวจ `scripts/thai/validate.py` ไม่พบข้อผิดพลาดด้านตัวแปร ตัวเลข รูปแบบข้อความ หรือคีย์ที่ขาด ความครอบคลุมนี้ไม่รวมข้อความจากระบบปฏิบัติการหรือส่วนที่ไม่ได้เรียกใช้ระบบแปล

รายงาน `i18n::tests::untranslated_report` ที่คอมไพล์จากซอร์ส 0.22.0 ไม่พบคีย์ภาษาไทยตกหล่น หลังเติมข้อความที่สแกนพบใหม่อีก 11 รายการ

ระบบตรวจอัปเดตชี้ไปที่ `tapanapon-com/vectorcraft-th` เพื่อไม่ให้รุ่นต้นฉบับทับคำแปล ช่องทางตรวจอัปเดตอาจไม่เสนอ prerelease ให้ดาวน์โหลดรุ่นทดลองจาก Releases โดยตรง

## ผลตรวจรุ่น 0.21.0-th.1

ผ่าน `cargo xtask ci` ครบทุกขั้น ชุดทดสอบ workspace ผ่าน 13,965 รายการ ไม่ผ่าน 0 รายการ และมี 15 รายการที่ต้นฉบับกำหนดให้ข้าม ทดสอบแอปจริงโดยบันทึก ปิด และเปิดไฟล์กลับ: โครงสร้างงานคงเดิม และไฟล์ PNG ก่อน/หลังเปิดกลับตรงกันทุกไบต์ การสลับภาษาไทย–อังกฤษไม่เปลี่ยนข้อมูลจาก `document.inspect`

ดูผลสรุปที่ [validation-th.json](validation-th.json) การทดสอบระบบฟอนต์ใช้โฟลเดอร์ชั่วคราวบน APFS เนื่องจากการทดสอบต้นฉบับอาศัยความละเอียดเวลาของระบบไฟล์

## เครดิต

- โค้ดและคำแปล: MIT OR Apache-2.0 พร้อมคง `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE` และ `ASSETS.md`
- ข้อความร่วม: [craft-i18n](https://github.com/storytold/craft-i18n), [FilmCraft TH](https://github.com/tapanapon-com/filmcraft-th), [PhotoCraft TH](https://github.com/tapanapon-com/photocraft-th)
- ฟอนต์: [craft-fonts](https://github.com/storytold/craft-fonts) ที่พิน `b076417b5880bd4154bd22f00695b1d28c6bea83` รวม Noto Sans Thai พร้อมใบอนุญาต OFL ในแพ็กเกจ ไม่เก็บไฟล์ฟอนต์ไว้ใน repository นี้
- ชื่อและตราสินค้าต้นฉบับอยู่ภายใต้เงื่อนไขของเจ้าของ

## สร้างและตรวจสอบ

```sh
export CRAFT_FONTS_DIR="$(cd ../craft-fonts && pwd)"
export CRAFT_FONTS_REQUIRED=1
python3 scripts/thai/validate.py
mkdir -p /private/tmp/vectorcraft-th-tests
TMPDIR=/private/tmp/vectorcraft-th-tests cargo xtask ci
cargo build --release --locked -p vectorcraft -p vectorcraft-cli
bash scripts/thai/package-local.sh
```

รุ่นที่สร้างด้วยสคริปต์นี้เป็นสถาปัตยกรรมของเครื่องที่ build เซ็นแบบ ad-hoc และยังไม่ผ่าน Apple notarization ไม่มีการอ้างว่าใช้แทน Illustrator ได้สมบูรณ์ ต้นฉบับยังระบุว่าเป็น alpha และมีข้อจำกัดเรื่อง `.ai` และความเที่ยงตรงในการแลกเปลี่ยนไฟล์ อ่าน `docs/gaps.md` ก่อนใช้งานจริง

## English

This is an independent Thai localization of [storytold/VectorCraft](https://github.com/storytold/vectorcraft), based on 0.22.0 at revision `654749c16eb20b6d3182a96defb66e11d1a9649a`. It is not an official or endorsed upstream release.

VectorCraft is a native Rust vector illustration application. Paths, anchors, shapes, text, layers and artboards are operated through a shared command engine used by the desktop UI, CLI and automation interface. The UI explicitly installs the bundled Noto Sans Thai face as a fallback in every UI font family. Thai text is embedded at build time; command identifiers and document contents retain their original values.

Choose Preferences › User Interface › Language › ไทย, or use `prefs.set` with `interfaceLanguage: "th"`. Regional Thai tags resolve to the Thai catalog. Thai uses one count-neutral plural form, including counted status messages.

The translation combines MIT/Apache-licensed sibling wording with a locally machine-assisted draft and terminology corrections. No Adobe application or proprietary localization resource was accessed. Some technical names and external diagnostics can remain in English. Catalog coverage does not prove that every dynamically generated message is translated.

The local package embeds official craft-fonts at revision `b076417b5880bd4154bd22f00695b1d28c6bea83`, including Noto Sans Thai, and bundles OFL notices. It is ad-hoc signed and not Apple-notarized. Upstream describes VectorCraft as alpha; do not assume complete Illustrator parity or lossless `.ai` round trips. Keep source files and review the upstream gaps before important work.

The Thai catalog contains 7,920 entries covering the reference catalogs and additional keys scanned from this source revision. The catalog validator reports zero missing keys or formatting/placeholder/number errors. The fresh compiled `i18n::tests::untranslated_report` lists no Thai or all-language gaps after adding 11 source-discovered strings. This is catalog coverage, not a guarantee about external or dynamically constructed diagnostics.

Build and validation commands appear above. Preserve upstream code, asset, font and branding notices when redistributing.


Update checks use `tapanapon-com/vectorcraft-th`, keeping upstream-only binaries out of this edition’s update channel. Prereleases may not be offered automatically; download them from Releases.

### Historical release validation — 0.21.0-th.1

`cargo xtask ci` passed every gate. The workspace test stage passed 13,965 tests with zero failures and 15 upstream-ignored tests. Native save/close/reopen preserved the document content summary and produced byte-identical PNG exports. Switching Thai/English preserved the full document inspection result. See [validation-th.json](validation-th.json). Filesystem timestamp-sensitive tests ran with a temporary directory on APFS.

## อัปเกรด 7 พฤศจิกายน 2026

รวมซอร์สต้นฉบับรุ่นใหม่และคงชุดแปลภาษาไทย ดูสถานะการตรวจและการแพ็กเกจใน [บันทึกอัปเกรด](thai-upgrade-20261107.md) ก่อนใช้ตัวเลขทดสอบรุ่นเก่าอ้างอิงรุ่นนี้

## ผลตรวจปัจจุบัน / Current source validation

Mac UI library: 3,279 passed, zero failed or ignored. Formatting and workspace/all-target Clippy passed. Full workspace CI and platform packaging are pending; see [current validation](validation-0.22.0-th.1.json). Earlier 13,965-test results above remain historical.
