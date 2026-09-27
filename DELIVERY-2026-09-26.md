# HJS / JEP delivery closeout — 2026-09-26

Updated on 2026-09-27 for the Agent SDK 2.1.5 scope/configuration patch; the dated audit sections below retain their original release and test evidence.

Initial audit: 29 repositories in `hjs-spec`. The subsequent architecture review covered the 28 remaining repositories after the owner deleted `hjs-05`. That review archived three documentation/demo repositories. The later [maintenance consolidation](CONSOLIDATION-2026-09-26.md) archived eight experiments, bringing the current total to 11 archived and 17 unarchived repositories. This review does not claim every companion implements Core 0.7.

## Simplification delivered

The [organization homepage](https://github.com/hjs-spec) now has three starting points: **protocol, Quickstart, integration**. The [public project directory](PROJECTS.md) distinguishes HTTP clients from local agent recording, separates optional experiments and research, and lists archived repositories with their maintained destinations.

Existing package names, imports and commands remain stable. Published protocol artifacts, signed historical data and frozen evidence were not rewritten. The local runtime keeps its own envelope and mock signatures; signed Core events use the Core/SDK/API path rather than being inferred from runtime labels.

Nine stale PRs were reviewed and closed after useful changes were absorbed or their superseding implementations verified: CLI #3, JS #8, Agent SDK #5, API #9, Runtime #7/#8, E2E demo #1, Architecture #3 and Quickstart #3. No open issues were returned by the organization-wide audit.

## Verified releases

| Component | Version | GitHub delivery | Additional delivery |
|---|---|---|---|
| Core conformance | 0.7.4 | [Python wheel/source + explicit legacy Go binaries](https://github.com/hjs-spec/jep-core/releases/tag/v0.7.4) | PyPI blocked: new package has no matching Trusted Publisher |
| CLI | 0.7.1 | [Wheel + source](https://github.com/hjs-spec/cli/releases/tag/v0.7.1) | Published to PyPI as `jep-cli` |
| Agent SDK | 2.1.5 | [Wheel + source](https://github.com/hjs-spec/jep-agent-sdk/releases/tag/v2.1.5) | Published to PyPI as `jep-agent-sdk` |
| Agent Blackbox | 0.3.0a3 | [Alpha wheel + source](https://github.com/hjs-spec/Agent-Blackbox/releases/tag/v0.3.0a3) | Published to PyPI as `agent-blackbox-jep` |
| JavaScript SDK | 0.7.1 | [npm-format tarball](https://github.com/hjs-spec/sdk-js/releases/tag/v0.7.1) | npm blocked by authentication; tarball is available |
| API | 0.8.4 | [Source release](https://github.com/hjs-spec/jep-api/releases/tag/v0.8.4) | GHCR image published; HF live deployment blocked by configuration |
| Go SDK | 0.7.1 | [Source + module tag](https://github.com/hjs-spec/sdk-go/releases/tag/v0.7.1) | Signed JSON transport repair |
| TSTO binding | 02 | [Experimental release bundle](https://github.com/cognitive-emergence/tsto-spec/releases/tag/jep-tsto-binding-02) | Frozen signed fixtures and reproduction report |
| Quickstart | 0.7.0 | [Wheel + source](https://github.com/hjs-spec/jep-quickstart/releases/tag/v0.7.0) | GitHub delivery; no new PyPI publisher configured |

API software 0.8.4 implements **Core 0.7**, not a new Core 0.8 protocol. Blackbox is explicitly an alpha prerelease. Python SDK 0.7.0 and Runtime 0.3.1 were already released and did not need another code release.

CLI, Agent SDK and Blackbox PyPI wheel/source SHA-256 values were compared with the corresponding GitHub assets and match.

Current API image: `ghcr.io/hjs-spec/jep-api:0.8.4`
Digest: `sha256:ba67a24871bd4187563c366498368e76fba860ac29db3d3fdb29f46449630450`

The earlier 0.8.0 release remains available (image digest `sha256:3093b66c116bcb1529262f12cd588e21e29aee587dc5d72325807d637f28aafb`).

The release workflow ran the actual built container and verified its health response, Core profile, software version and source revision before pushing it.

## Initial repairs and verification

- CLI: removed the obsolete universal audience requirement from its acceptance regression expectations, preserved explicit historical formats, verified invalid/indeterminate exit codes, and fixed large inline JSON handling. **11 local tests passed.**
- API: included current schema in Docker/HF packages, synchronized the repaired Core schema, returned indeterminate for unavailable verification keys, and validated TTL/digest-only extensions before acceptance. **93 local tests passed; hosted CI also exercised PostgreSQL multi-host state.**
- Quickstart: pinned the tested current API commit, fixed the LangGraph example's removed `nonce` access, and checked syntax alongside signature/identity during replay. **12 real HTTP integration/example tests passed.**
- Agent SDK: published the import, conformance, strict validation and report repairs from the preceding handoff. **71 local tests, lint/format, installed-package coexistence and independent conformance checks passed.**
- Blackbox: aligned VERSION, package and Action versions; required protected `kid`; passed Action input through environment variables. **12 tests passed.**
- JavaScript SDK: corrected stale release notes and verified package metadata. **7 tests passed.**
- Core: current/legacy Python checks and frozen-draft checks passed. The first 0.7.1 delivery attempt exposed a legacy Go test accidentally reading the current manifest; earlier CI had reused a cached result. The repair selects `test-manifest-0.6.json` explicitly and uses `go test -race -count=1` in both CI and release. The full uncached hosted matrix passed; the 0.7.2 release job then passed and published its artifacts.
- Python publication checks VERSION against pyproject, wheel metadata and source metadata. Workflow-only edits no longer trigger publication. Existing releases are never overwritten.
- Architecture documents and their checked-in SVG preview now describe Core 0.7 independent checks.

## Architecture review and follow-up

The follow-up simplifies maintained entry points and resolves contradictory current guidance:

- Core 0.7 and historical 0.6 sources are explicitly separated. Schemas are described as reference implementation aids, not independent normative definitions.
- A single [format and verification matrix](https://github.com/hjs-spec/jep-core/blob/main/docs/architecture/architecture-notes.md#format-and-verification-matrix) records actual wire/archive formats. Local runtime, visualization and signature claims no longer imply universal Core interoperability.
- API deployment and JS publication instructions now match their workflows. SDK/CLI notices, contribution commands and research entry points were corrected; old migration/interop reports are explicitly historical.
- Core, Runtime and whitepaper landing pages were shortened. The original whitepaper body, published drafts and historical signatures remain unchanged.
- `jep-architecture`, `jep-vs-logging` and `jep-e2e-demo` were verified with `archived: true`. Current documentation lives in Core and current onboarding lives in Quickstart.
- [API PR #11](https://github.com/hjs-spec/jep-api/pull/11) fixes a real migration omission: accepted Event Identities were not copied from SQLite to PostgreSQL. The import now preserves them, remains idempotent and rolls back on conflicting accepted content. **97 tests passed with real PostgreSQL**, including the migration regression cases.

API [release run](https://github.com/hjs-spec/jep-api/actions/runs/36246530266) published software 0.8.1 source and the health-tested GHCR image. Live HF deployment remains blocked by the configuration below. Documentation-only changes created no additional software versions. All configured component PR checks passed; the Core frozen -07 SHA-256 check passed and edited local documentation links were verified.

## Core 0.7 / Binding/02 follow-up audit

Rechecked the 28 remaining `hjs-spec` repositories and related TSTO/research entry points after Binding/02. Independent experimental formats and frozen research baselines remain separate; this is an upgrade/dependency review, not a claim of universal conformance.

Confirmed omissions were repaired and released:

- [Go SDK #6](https://github.com/hjs-spec/sdk-go/pull/6): preserve signed empty optional members, unknown members and numeric tokens during JSON roundtrips. Explicit `scope`/`result` null values remain present for profile evaluation. Uncached race tests passed.
- [Core #26](https://github.com/hjs-spec/jep-core/pull/26), [API #12](https://github.com/hjs-spec/jep-api/pull/12) and [Agent SDK #9](https://github.com/hjs-spec/jep-agent-sdk/pull/9): malformed identities now return schema-valid `event_identity: null` rejection diagnostics, without applying acceptance effects.
- Core, API, Agent SDK and [Blackbox #6](https://github.com/hjs-spec/Agent-Blackbox/pull/6): preserve signatures/hashes when a large JCS number is serialized as an integer token by JavaScript. Both exact binary64 integer values and their canonical shortest-decimal spellings are accepted; other precision-losing integers and overflow remain rejected; timestamp bounds remain unchanged.
- [API #13](https://github.com/hjs-spec/jep-api/pull/13): use `VERSION` as the single runtime version source and include it in Docker/HF bundles. The 0.8.2 release guard caught a stale duplicated constant and stopped before publication. Software 0.8.3 was then published successfully; no 0.8.2 release/image exists.
- [TSTO #8](https://github.com/cognitive-emergence/tsto-spec/pull/8): distinguish original release reproduction from current software checks. Current entry points can evolve while the original manifest, frozen specifications, schemas, fixtures, harness and published assets remain unchanged.
- Current installation guides use the available package release; [Quickstart #6](https://github.com/hjs-spec/jep-quickstart/pull/6) advances its tested API pin to 0.8.4. These documentation/CI updates need no extra package version.

A final numeric boundary check found that the first repair still rejected canonical shortest decimal tokens such as `1000000000000000100`. [Core #28](https://github.com/hjs-spec/jep-core/pull/28), [API #14](https://github.com/hjs-spec/jep-api/pull/14), [Agent SDK #11](https://github.com/hjs-spec/jep-agent-sdk/pull/11) and [Blackbox #8](https://github.com/hjs-spec/Agent-Blackbox/pull/8) complete that repair with positive/negative and boundary-number regressions. Earlier releases remain immutable.

The independent [TSTO research validation plan](https://github.com/cognitive-emergence/tsto-spec/pull/1) remains a draft; it does not modify Binding/02 and is not evidence that its proposed research gates have passed.

The [maintained interoperability gate](https://github.com/hjs-spec/jep-core/tree/main/integration#current-core-07--binding02) pins companion commits and checks 11 signed events through 5 serialization paths: **55 exact signature/hash roundtrips**, four verifier implementations, **50 Binding/02 structural/reference checks**, and malformed-identity result schemas. It tests Core-valid but wrong-policy carriers separately. Domain policy, external truth and deployed acceptance are not implied by these checks. Both the new gate and the retained current/legacy Core matrix passed in hosted CI.

API **99 tests passed with PostgreSQL**; Agent SDK **73 tests plus lint/format/coexistence passed**; Blackbox **13 tests passed**; Quickstart **12 real HTTP tests passed** against 0.8.4. Agent SDK 2.1.3 and Blackbox 0.3.0a3 PyPI wheel/source hashes match their GitHub assets.

[API release run](https://github.com/hjs-spec/jep-api/actions/runs/36250336967) published source and the health-checked 0.8.4 image above. Core 0.7.4, Agent SDK 2.1.3, Blackbox 0.3.0a3 and Go SDK 0.7.1 GitHub assets were verified. The remaining registry/deployment configuration blocks are listed below.

## Viewer/archive follow-up — 2026-09-27

[Agent SDK #13](https://github.com/hjs-spec/jep-agent-sdk/pull/13) fixes three reproducible gaps in the maintained local recording/report path:

- Browser imports reject duplicate members, unsupported precision-losing integers, non-finite numbers and invalid Unicode/UTF-8. The upload endpoint uses the SDK's strict parser and returns a client error with the failing line for malformed event JSON.
- Exported viewer HTML embeds escaped event data and restores the interactive archive when reopened. Reset View preserves the restored events; reports remain unverified projections.
- Report links require matching artifact pins. Conflicting artifacts sharing an Event Identity remain unresolved without an exact pin, and CLI reports also resolve digest references.

All **90 SDK tests**, the Python 3.10–3.13 matrix, lint/format, signing/persistence/tamper checks and package coexistence passed. The [2.1.4 release workflow](https://github.com/hjs-spec/jep-agent-sdk/actions/runs/36285778002) published GitHub and PyPI artifacts. Wheel and source hashes match across both registries, and the downloaded PyPI wheel contains the fixed viewer and CLI source. Protocol formats and frozen drafts are unchanged.

The audit also compared the other primary source trees with their current release tags. No additional unshipped runtime changes were found; later changes were documentation or CI pins. Current Core conformance and interoperability checks passed in hosted CI. The remaining configuration blocks below are separate from the viewer fix; the Core 0.7.4 PyPI and JavaScript 0.7.1 npm version endpoints still returned 404 on this follow-up check.

## Protocol-scope follow-up — 2026-09-27

Reviewed 611 tracked paths across the 16 public, unarchived HJS repositories and
TSTO, against their current main branches. No generated-cache/build-directory or
temporary-file candidates were found in that tracked inventory. The maintained
code and dependency scan found no imports of the independent AIP sidecar or MCP
filtering experiment. This is a scoped repository review, not a proof that every
implementation defect is absent. Private baselines and Prooftask were unchanged.

- [Core #31](https://github.com/hjs-spec/jep-core/pull/31),
  [MCP filter #3](https://github.com/hjs-spec/shutup-mcp/pull/3), and
  [AIP sidecar #4](https://github.com/hjs-spec/aip-judgment-sidecar/pull/4) make the
  independent-project boundaries explicit. [PROJECTS.md](PROJECTS.md) separates
  optional protocol companions, historical workflow integration and independent
  experiments outside JEP/TSTO. Existing packages and source histories are retained;
  this step neither deletes nor archives additional repositories.
- [Agent SDK #14](https://github.com/hjs-spec/jep-agent-sdk/pull/14) rejects invalid
  determinability-guard conflict modes and missing/noncallable fallback handlers.
  These configurations previously executed guarded calls despite a modeled
  conflict. Callable falsey handlers now run correctly; explicit `warn` remains
  an allow mode. Finite-model helpers are research compatibility APIs, outside
  Core/TSTO verification; an empty knowledge base performs no comparison.
- The SDK architecture entry now documents the current components instead of the
  historical 2.0.x layer stack. The research example uses actual call arguments.
  Viewer deployment installs the base SDK without unused framework extras or a
  compiler; the unused archive mount and storage environment setting are removed.

All **99 SDK tests**, Python 3.10–3.13, lint/format, package coexistence and the
actual Compose build/HTTP viewer check passed. The first container check exposed
a startup connection-reset race in the new test; bounded retries resolved it and
the final PR and main CI passed. Core conformance/interoperability and both
independent-project documentation PR workflows also passed.

The [2.1.5 release workflow](https://github.com/hjs-spec/jep-agent-sdk/actions/runs/36286694418)
published GitHub and PyPI artifacts. Both registries have identical wheel/source
SHA-256 values. The downloaded PyPI wheel contains the exact repaired guard and
version source. Published drafts, signed event formats and TSTO fixtures remain
unchanged; existing external configuration blockers below remain separate.

## External configuration still required

### npm

[Publication attempt](https://github.com/hjs-spec/sdk-js/actions/runs/36243899535) failed with `ENEEDAUTH`. Configure a publisher authorized for `@hjs-spec/jep-sdk-js` (the workflow currently accepts the repository's `NPM_TOKEN` secret or an appropriately configured trusted publisher), then rerun **failed jobs only**. The GitHub release already exists and must not be recreated.

The released tarball can be installed directly:

```sh
npm install https://github.com/hjs-spec/sdk-js/releases/download/v0.7.1/hjs-spec-jep-sdk-js-0.7.1.tgz
```

### Hugging Face live API

[Latest deployment attempt](https://github.com/hjs-spec/jep-api/actions/runs/36250428061) authenticated successfully but stopped **before upload** because the existing Space `yuqiangJEP/jep-api` lacks:

- Variable `JEP_DEPLOYMENT_MODE=production`.
- Secrets `JEP_DATABASE_URL` and `JEP_SIGNING_TOKEN`.
- Secret `JEP_KEYRING_JSON`, or the complete HTTPS Vault signing configuration documented by the API deployment script.

Use the intended production database and signing identity; do not generate replacement keys merely to satisfy this gate. After configuration, rerun the failed deployment and verify health reports API version `0.8.4`, Core profile `jep-core-0.7`, and revision `0ed259f8f137f57c8122487ba44e0dcfce5bc172`.

### Core conformance on PyPI

The [0.7.4 GitHub release](https://github.com/hjs-spec/jep-core/releases/tag/v0.7.4) is complete. [PyPI publication](https://github.com/hjs-spec/jep-core/actions/runs/36250416658) failed with `invalid-publisher`: the OIDC token was valid but no publisher matched it.

Configure the intended PyPI project `jep-core-conformance` with a Trusted Publisher for owner `hjs-spec`, repository `jep-core`, workflow `release.yml` (no GitHub environment is selected by this workflow). Then rerun **failed jobs only** for the existing run, so the successful immutable GitHub release and Go tag are preserved.

The available wheel can already be installed directly:

```sh
python -m pip install https://github.com/hjs-spec/jep-core/releases/download/v0.7.4/jep_core_conformance-0.7.4-py3-none-any.whl
```

## Frozen publication

The published Core Internet-Draft -07 remains byte-for-byte unchanged. Its RFCXML SHA-256 is:

`601809b4053d485fa68367db22f5e43919e859c4f0227609b8f851c627e9caab`

Software patch versions do not modify that Internet-Draft or rewrite historical signed events.
