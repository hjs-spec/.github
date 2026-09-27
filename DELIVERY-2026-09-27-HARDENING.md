# Core 0.7 implementation hardening — 2026-09-27

This supersedes the recommended software combination in the [earlier same-day closeout](DELIVERY-2026-09-27.md). That report remains an unchanged record of its earlier checks. This is a software patch, not a new Internet-Draft revision.

## Merged and published

| Component | Delivery | Change and merged source |
|---|---|---|
| Core conformance | 0.7.5, GitHub and PyPI | [Core #33](https://github.com/hjs-spec/jep-core/pull/33), `ab68571276e5e2a2b37ae1ffc38cc95d0d3deda7` |
| Agent SDK | 2.1.6, GitHub and PyPI | [Agent SDK #15](https://github.com/hjs-spec/jep-agent-sdk/pull/15), `3c203d7005ff1c5fb55591fad5019254d092e826` |
| Reference API | 0.8.5, GitHub source | [API #15](https://github.com/hjs-spec/jep-api/pull/15), `14a09cdd3ee9ded13996264cb3158c3cec332f44` |
| HTTP Quickstart | Documentation and CI updated; package remains 0.7.0 | [Quickstart #7](https://github.com/hjs-spec/jep-quickstart/pull/7), `36037e7fad40e048ea3128bcb00499cc8ff2e055` |

Python HTTP SDK 0.7.0, CLI 0.7.2, Go HTTP SDK 0.7.2 and the JavaScript 0.7.1 GitHub tarball remain in the tested combination. No unchanged package was re-uploaded.

## Repairs

Current structural schemas now reject empty extension identifiers and digest strings with trailing line terminators, matching the hand-written validators. Current API JWS verification validates decoded header values for malformed Unicode and unsupported numbers. Agent SDK current JWS verification explicitly requires UTF-8 rather than JSON encoding auto-detection.

The original protected-header bytes remain the signing input. Valid noncanonical UTF-8 JSON headers are not rejected merely for whitespace, ordering or a different canonical representation. Explicit legacy profile decoding is preserved.

A new shared test gate runs 25 real-signature cases through Core, API and Agent SDK. Before the paired fixes, 14 cases had inconsistent results; afterward all 25 passed. This counts test cases, not 14 distinct vulnerabilities. The gate checks archival and acceptance outcomes, failed-check diagnostic categories, unchanged hashes, rejection without consuming an Event Identity, and corrected acceptance followed by an idempotent retry.

## Hosted validation evidence

- [API full regression and PostgreSQL state](https://github.com/hjs-spec/jep-api/actions/runs/36293148489): **117 passed**; one dependency deprecation warning.
- [Agent SDK CI](https://github.com/hjs-spec/jep-agent-sdk/actions/runs/36293374400): passed. [Merged release and PyPI publishing](https://github.com/hjs-spec/jep-agent-sdk/actions/runs/36293701870): passed, including lint, tests, build and package coexistence.
- [Core current/legacy conformance](https://github.com/hjs-spec/jep-core/actions/runs/36293615367): passed, including frozen-publication checks.
- [Merged cross-repository interoperability](https://github.com/hjs-spec/jep-core/actions/runs/36293788840): passed, retaining **55 signed-artifact roundtrips**, **50 Binding/02 structural/reference checks**, and adding the **25-case hostile-input gate**.
- [Quickstart installed package/local API](https://github.com/hjs-spec/jep-quickstart/actions/runs/36293715962): passed against the pinned repaired API.
- [Core publication and post-publication installs](https://github.com/hjs-spec/jep-core/actions/runs/36293788880): GitHub publication, PyPI publication and **Linux, Windows and macOS** install jobs all passed. These jobs downloaded the new 0.7.5/2.1.6 combination, not the older baseline used during PR checks.

The post-publication reports retain platform, Python version, exact package versions, download locations, SHA-256 digests, installed dependencies and smoke-test output. Eight Python release files were downloaded independently from PyPI and GitHub and compared with both metadata and actual bytes. Five supplementary release files were also checked: **13 original release files total**. Third-party dependencies are not an offline bundle.

Installed smoke tests passed J/D/T/V signatures, four Core/SDK/CLI roundtrips, eight tamper rejections, eighteen malformed-input rejections, missing-key `indeterminate`, and accepted/already-accepted/identity-conflict behavior.

Selected release digests:

| Artifact | SHA-256 |
|---|---|
| Core 0.7.5 wheel | `a6cc035fd9d6cfcaf2084e86f7ff3491e533f235fe0301d7139bc7a001ee05c2` |
| Agent SDK 2.1.6 wheel | `0a6b397031a4914a2389f0f61d86d36cbc3fcefe50b43af1a1049d11736ce686` |
| API 0.8.5 source | `dc7266faebd79e1a871a7181033e37a1e3ee464dddeb62baf055e22f04999c22` |

## First-use path

The default [local example](https://github.com/hjs-spec/jep-agent-sdk#local-create--export--independent-verification) creates a signed event, exports its public JWK and PEM, and verifies it in a separate process. It does not require an API or export a private key. Tests reject tampering, missing public keys and accidental overwrites. A second, independently implemented Core verifier can check the same event and JWK file.

[HTTP Quickstart](https://github.com/hjs-spec/jep-quickstart) is explicitly separate and pins the user-facing release combination. The organization directory and homepage distinguish these two paths rather than making a hosted API a prerequisite for every first use.

## Unchanged boundaries and remaining configuration

The protocol remains **JEP Core 0.7 / Internet-Draft -07 / wire major 1**. Frozen -07 RFCXML SHA-256 is still `601809b4053d485fa68367db22f5e43919e859c4f0227609b8f851c627e9caab`. Frozen TSTO/Binding artifacts, historical signed fixtures and Prooftask were not modified. Historical decoder selection remains explicit; failed current validation never authorizes fallback.

This is not an exhaustive security audit, independent external adoption, proof of actor identity or truth, domain-policy validation, or confirmation of a deployed production service. Public demonstration keys establish signature consistency, not a trusted real-world identity. Agent SDK acceptance remains single-process reference state.

No new PyPI authorization is needed. npm publishing authorization and optional hosted API production configuration remain separate [owner configuration items](CONFIGURATION-HANDOFF-2026-09-27.md); this work does not claim those are complete. No production credential or acceptance-state reset was performed.
