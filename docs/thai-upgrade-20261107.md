# Vectorcraft Thai upgrade 7 November 2026

Upstream release: https://github.com/storytold/vectorcraft/releases/tag/v0.22.0

Thai distribution being prepared: 0.22.0-th.1. Based on the complete upstream release tag, preserving its engine and format crate versions. Existing Thai translations remain, with new source strings translated. Current Thai catalog: 7,920 entries.

Catalog validation passed. Native build, platform packaging and integration checks are in progress. This record does not claim that installers have been released or that all upstream functionality has been tested. Previous 0.21.0 validation reports remain historical.

Mac builds are ad-hoc signed and are not Apple-notarized. Windows builds are unsigned. Build one job at a time.

## Mac source checks

Catalog: 7,920 entries, adding 107. The compiled source report has no Thai gaps and no all-language gaps after translating 11 additional source-discovered keys. All 3,279 Mac UI library tests passed with zero failures or ignored tests. Formatting and workspace/all-target Clippy passed. Full local workspace compilation was interrupted twice because swap growth exhausted system disk space, not because a source test failed. The complete shared gate passed on Ubuntu:14,487 tests passed,15 skipped and all12stages passed. See https://github.com/tapanapon-com/vectorcraft-th/actions/runs/42376413663. Only documentation changes follow that tested source tree; native packages are checked separately before publication. The validated source merge is checkpointed on the upgrade branch; it is not a release or default-branch publication.
