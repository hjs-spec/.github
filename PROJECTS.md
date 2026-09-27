# Repository directory

One protocol source, one runnable introduction, and an integration chosen for your application. This is the organization-wide directory; component READMEs describe their own interfaces.

## Start

| Repository | Responsibility |
|---|---|
| [jep-core](https://github.com/hjs-spec/jep-core) | Core specification, schemas, conformance vectors and reference validators |
| [jep-quickstart](https://github.com/hjs-spec/jep-quickstart) | Default local introduction: create a signed event and verify its archive |

## Integrate

Choose **HTTP** when a service owns signing and acceptance state. Choose **local recording** when the application owns its signing key and records agent calls.

| Path | Repository | Responsibility |
|---|---|---|
| HTTP service | [jep-api](https://github.com/hjs-spec/jep-api) | Core 0.7 signing, verification, storage and acceptance state |
| HTTP client | [sdk-py](https://github.com/hjs-spec/sdk-py) | Python client |
| HTTP client | [sdk-js](https://github.com/hjs-spec/sdk-js) | JavaScript client; use the documented GitHub tarball while npm publication is blocked |
| HTTP client | [sdk-go](https://github.com/hjs-spec/sdk-go) | Go client |
| HTTP client | [cli](https://github.com/hjs-spec/cli) | Command-line client |
| Local recording | [jep-agent-sdk](https://github.com/hjs-spec/jep-agent-sdk) | Signed Core 0.7 agent records, local verification and reports |
| Completion binding | [tsto-spec](https://github.com/cognitive-emergence/tsto-spec) | TSTO/00 + JEP Core 0.7 + experimental Binding/02; completion policy stays with the application |

`sdk-py` calls a service; `jep-agent-sdk` records locally. They are different interfaces, not two competing protocol definitions. Local acceptance is single-process; use the API with shared PostgreSQL state when acceptance must span hosts.

<a id="optional-components"></a>

## Optional protocol companions

These components support JEP/HJS/JAC investigation but are not required for the
current JEP/TSTO path. A common J/D/T/V vocabulary or JSONL extension does not make
formats interchangeable. Check the [format matrix](https://github.com/hjs-spec/jep-core/blob/main/docs/architecture/architecture-notes.md#format-and-verification-matrix) before connecting them.

| Repository | Purpose / boundary |
|---|---|
| [Agent-Blackbox](https://github.com/hjs-spec/Agent-Blackbox) | Alpha incident recorder; Core 0.7-style events with local JAC/HJS conventions |
| [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) | JAC declarations and fragment checks; pinned historical demo events |

## Historical workflow integration

[jep-github-action](https://github.com/hjs-spec/jep-github-action) retains a Core 0.6
workflow integration. It is protocol-related, but not the current onboarding path.
Use Quickstart and the current integration choices above for new deployments.

## Independent experiments outside JEP/TSTO

Organization membership is not protocol scope. The repositories below are not
JEP/TSTO implementations, optional conformance requirements, or dependencies of
the maintained protocol path. They retain their own source and published packages;
no format migration or capability transfer is implied.

| Repository | Actual purpose | Relationship to this protocol |
|---|---|---|
| [shutup-mcp](https://github.com/hjs-spec/shutup-mcp) | General MCP tool-list filtering | Unrelated to JEP events, TSTO objects, signatures or binding validation |
| [aip-judgment-sidecar](https://github.com/hjs-spec/aip-judgment-sidecar) | Independent AIP receipt and policy-hook prototype | Adjacent research; its signed receipt is not a JEP event and has no TSTO binding |

Keep independent product work outside the JEP/TSTO feature roadmap. A future
protocol integration needs an explicit mapping and interoperability checks first.

## Research and organization

| Repository | Responsibility |
|---|---|
| [whitepaper](https://github.com/hjs-spec/whitepaper) | Original conceptual paper; published body preserved |
| [jep-papers-and-corpus](https://github.com/hjs-spec/jep-papers-and-corpus) | Versioned research and exploratory corpus; not a conformance suite |
| [.github](https://github.com/hjs-spec/.github) | Organization homepage, this directory and delivery records |

## Retired experiments

These eight repositories left active development on 2026-09-26 and are retained
read-only for reproduction. Their original formats, readers, releases and histories
remain available. New signed recording and reports belong to the
[Agent SDK](https://github.com/hjs-spec/jep-agent-sdk/blob/main/docs/INTEGRATIONS.md).
That guide lists capability gaps and the original reader required for each archive;
it does not promise automatic migration or equivalent framework hooks.

| Repository | Preserved capability / boundary |
|---|---|
| [jep-runtime](https://github.com/hjs-spec/jep-runtime) | Local policy/replay experiment; own envelope and mock signatures |
| [jep-langgraph-adapter](https://github.com/hjs-spec/jep-langgraph-adapter) | LangGraph observation; own unsigned archive format |
| [jep-openai-agents-middleware](https://github.com/hjs-spec/jep-openai-agents-middleware) | Agents SDK observation; own unsigned archive format |
| [jep-mcp-wrapper](https://github.com/hjs-spec/jep-mcp-wrapper) | MCP callable observation; own unsigned archive format |
| [jep-authority-runtime](https://github.com/hjs-spec/jep-authority-runtime) | Declared authority policy model; no Core signature verification |
| [jep-replay-visualizer](https://github.com/hjs-spec/jep-replay-visualizer) | Browser projection of supplied records; no cryptographic verification |
| [jep-lineage-explorer](https://github.com/hjs-spec/jep-lineage-explorer) | Declared lineage and scope checks; no cryptographic verification |
| [jep-claude-replay](https://github.com/hjs-spec/jep-claude-replay) | Claude transcript/replay prototype; own signatures and `.jcrpack` format |

[Consolidation decision and evidence](CONSOLIDATION-2026-09-26.md).

## Earlier documentation archives

These three were set read-only in the earlier consolidation on 2026-09-26. Original histories and releases remain available.

| Archived repository | Maintained destination |
|---|---|
| [jep-architecture](https://github.com/hjs-spec/jep-architecture) | [Core architecture](https://github.com/hjs-spec/jep-core/tree/main/docs/architecture) |
| [jep-vs-logging](https://github.com/hjs-spec/jep-vs-logging) | [Core logging comparison](https://github.com/hjs-spec/jep-core/blob/main/docs/comparisons/logging.md) |
| [jep-e2e-demo](https://github.com/hjs-spec/jep-e2e-demo) | [Quickstart](https://github.com/hjs-spec/jep-quickstart); old Core 0.6 example preserved |

HJS documentation is available at the [public draft](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/). The owner deleted `hjs-05`; it is not a current dependency or installation step. Historical source pins remain historical evidence.

## Maintenance rules

1. Protocol definitions, schemas and conformance vectors live in Core. Downstream copies pin their source revision.
2. New users follow Quickstart. Other repositories link to it instead of copying a full onboarding stack.
3. Every component states its format and actual verification scope. Never infer Core conformance from a name or a successful local replay.
4. Keep existing package names and commands stable. Merge implementation code only after format compatibility and a consumer migration path are proven.
5. Preserve published drafts, signed artifacts and research baselines. Code fixes receive new software releases; documentation-only changes need no package version.
6. Keep retired experiments outside the active feature roadmap. Reopening requires a concrete consumer, a named format and a maintenance owner.
7. Keep generic tool filtering, independent receipt formats and finite-model research guards outside Core requirements and the default integration path. SDK research imports remain available for compatibility, without a conformance claim.
8. Add capability to its existing owner before creating a repository. [Portable evidence](https://github.com/hjs-spec/jep-core/blob/main/docs/decisions/portable-evidence-repository.md) starts in the SDK.

[Current interoperability checks](https://github.com/hjs-spec/jep-core/tree/main/integration#current-core-07--binding02) verify signed artifacts across Core, clients, API and local recorders.

[Delivery status](DELIVERY-2026-09-26.md) distinguishes GitHub releases, registries, containers and live deployments. [Consolidation provenance](https://github.com/hjs-spec/jep-core/blob/main/docs/REPOSITORY-CONSOLIDATION-2026-09.md) records the documentation move.
