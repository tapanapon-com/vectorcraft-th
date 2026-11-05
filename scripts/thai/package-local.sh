#!/usr/bin/env bash
# Package the native host build for local testing. No notarization or Developer ID claim.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DIST="$ROOT/dist/thai"
APP="$DIST/VectorCraft.app"
STAGE="$DIST/dmg-stage"
VERSION=0.21.0-th.1
ARCH="$(uname -m)"
BINARY="$ROOT/target/release/vectorcraft"
[[ -x "$ROOT/target/release/vectorcraft-cli" ]] || { echo 'Build vectorcraft-cli --release first.' >&2; exit 1; }
[[ -x "$BINARY" ]] || { echo 'Build vectorcraft --release first.' >&2; exit 1; }
CRAFT_FONTS_DIR="${CRAFT_FONTS_DIR:-$ROOT/../craft-fonts}"
mkdir -p "$APP/Contents/Resources/Licenses"
for license in "$CRAFT_FONTS_DIR"/fonts/*/OFL.txt; do
  [[ -f "$license" ]] || continue
  family="$(basename "$(dirname "$license")")"
  cp "$license" "$APP/Contents/Resources/Licenses/OFL-$family.txt"
done
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources" "$STAGE"
cp "$BINARY" "$APP/Contents/MacOS/VectorCraft"
cp "$ROOT/target/release/vectorcraft-cli" "$APP/Contents/MacOS/vectorcraft-cli"
cp "$ROOT/assets/app-icon/vectorcraft.icns" "$APP/Contents/Resources/VectorCraft.icns"
cp "$ROOT/NOTICE" "$ROOT/ASSETS.md" "$ROOT/LICENSE-MIT" "$ROOT/LICENSE-APACHE" "$APP/Contents/Resources/"
cp "$ROOT/docs/localization-th.md" "$ROOT/docs/validation-th.json" "$ROOT/ATTRIBUTION.md" "$APP/Contents/Resources/"
sed -e "s/@VERSION@/$VERSION/g" -e 's/@SHORT_VERSION@/0.21.0/g' \
  -e "s/@BUILD_SHA@/$(git -C "$ROOT" rev-parse --short HEAD)-thai/g" \
  "$ROOT/packaging/macos/Info.plist.in" > "$APP/Contents/Info.plist"
printf 'APPL????' > "$APP/Contents/PkgInfo"
plutil -lint "$APP/Contents/Info.plist"
xattr -cr "$APP"
lipo "$APP/Contents/MacOS/VectorCraft" -verify_arch "$ARCH"
codesign --force --sign - --timestamp=none --identifier ai.storyteller.vectorcraft-cli "$APP/Contents/MacOS/vectorcraft-cli"
codesign --force --sign - --timestamp=none "$APP/Contents/MacOS/VectorCraft"
codesign --force --sign - --timestamp=none "$APP"
codesign --verify --deep --strict "$APP"
ditto "$APP" "$STAGE/VectorCraft.app"
[[ -L "$STAGE/Applications" ]] || ln -s /Applications "$STAGE/Applications"
DMG="$DIST/VectorCraft-TH-$VERSION-macOS-$ARCH.dmg"
# A filesystem image preserves executable metadata when mounted.
hdiutil create -ov -fs HFS+ -format UDZO -srcfolder "$STAGE" -volname 'VectorCraft Thai' "$DMG"
hdiutil verify "$DMG"
(cd "$DIST" && shasum -a 256 "$(basename "$DMG")" > "$(basename "$DMG").sha256")
echo "Local ad-hoc build (not notarized): $DMG"
