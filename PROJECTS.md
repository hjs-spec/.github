# Repository directory

Choose the task you want to complete. Each entry includes runnable commands and expected results.

## Start

| I want to… | Start with |
|---|---|
| Verify a sample event | [Core sample](https://github.com/hjs-spec/jep-core#verify-your-first-event): install the verifier and check a packaged signature |
| Record my own events locally | [Agent SDK example](https://github.com/hjs-spec/jep-agent-sdk#local-create--export--independent-verification): create, export and verify a signed event |
| Use an HTTP service | [HTTP Quickstart](https://github.com/hjs-spec/jep-quickstart): start a local API and call it from a client |
| Build an independent implementation | [Implementer guide](https://github.com/hjs-spec/jep-core/blob/main/docs/IMPLEMENTER-GUIDE.md), then [BYOI tests](https://github.com/hjs-spec/jep-core/blob/main/docs/BYOI-CONFORMANCE.md) |

## Integrate

Choose **HTTP** when a service owns signing and acceptance state. Choose **local recording** when the application owns its signing key and records agent calls. For HTTP integration, self-host the reference API and configure its endpoint.

| Path | Repository | Responsibility |
|---|---|---|
| HTTP service | [jep-api](https://github.com/hjs-spec/jep-api) | Self-hostable Core 0.7 signing, verification, storage and acceptance state |
| HTTP client | [sdk-py](https://github.com/hjs-spec/sdk-py) | Python client |
| HTTP client | [sdk-js](https://github.com/hjs-spec/sdk-js) | JavaScript client; npm package `@hjs-api-db/jep-sdk-js` |
| HTTP client | [sdk-go](https://github.com/hjs-spec/sdk-go) | Go client |
| HTTP client | [cli](https://github.com/hjs-spec/cli) | Command-line client |
| Local recording | [jep-agent-sdk](https://github.com/hjs-spec/jep-agent-sdk) | Signed Core 0.7 agent records, local verification and reports |
| Completion binding | [tsto-spec](https://github.com/cognitive-emergence/tsto-spec) | TSTO/00 + JEP Core 0.7 + experimental Binding/02; completion policy stays with the application |

`sdk-py` calls a service; `jep-agent-sdk` records locally. They are different interfaces, not two competing protocol definitions. Local acceptance is single-process; use the API with shared PostgreSQL state when acceptance must span hosts.

<a id="optional-components"></a>
<a id="optional-protocol-companions"></a>

## Optional tools

Use these for incident review or declared dependency fragments. Their supported
formats and checks are listed in the [format matrix](https://github.com/hjs-spec/jep-core/blob/main/docs/architecture/architecture-notes.md#format-and-verification-matrix).

| Repository | Purpose / boundary |
|---|---|
| [Agent-Blackbox](https://github.com/hjs-spec/Agent-Blackbox) | Alpha incident recorder; local evidence digests, declared links and integrity checks |
| [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) | JAC declarations and fragment checks; pinned historical demo events |

## Historical workflow integration

[jep-github-action](https://github.com/hjs-spec/jep-github-action) was archived on
2026-09-30 (UTC). Its Core 0.6 source, tags and releases remain available for
historical workflows and regression reproduction.

## Research and organization

| Repository | Responsibility |
|---|---|
| [whitepaper](https://github.com/hjs-spec/whitepaper) | Original conceptual paper; published body preserved |
| [jep-papers-and-corpus](https://github.com/hjs-spec/jep-papers-and-corpus) | Versioned research and exploratory corpus; not a conformance suite |
| [.github](https://github.com/hjs-spec/.github) | Organization homepage, this directory and delivery records |

## Retired experiments

Eight runtime, replay and observation experiments were archived on 2026-09-26.
Their [repository list and retirement evidence](CONSOLIDATION-2026-09-26.md)
and [original readers and migration limits](https://github.com/hjs-spec/jep-agent-sdk/blob/main/docs/INTEGRATIONS.md#existing-experimental-archives)
remain available for reproduction.

## Earlier documentation archives

These three were set read-only in the earlier consolidation on 2026-09-26. Original histories and releases remain available.

| Archived repository | Maintained destination |
|---|---|
| [jep-architecture](https://github.com/hjs-spec/jep-architecture) | [Core architecture](https://github.com/hjs-spec/jep-core/tree/main/docs/architecture) |
| [jep-vs-logging](https://github.com/hjs-spec/jep-vs-logging) | [Core logging comparison](https://github.com/hjs-spec/jep-core/blob/main/docs/comparisons/logging.md) |
| [jep-e2e-demo](https://github.com/hjs-spec/jep-e2e-demo) | [Quickstart](https://github.com/hjs-spec/jep-quickstart); old Core 0.6 example preserved |

[Current interoperability checks](https://github.com/hjs-spec/jep-core/tree/main/integration#current-core-07--binding02) verify signed artifacts across Core, clients, API and local recorders.

[Current delivery status](DELIVERY-CURRENT.md) distinguishes GitHub releases, registries, containers, owner-confirmed account settings and actual live deployments. Dated reports remain historical evidence. [Consolidation provenance](https://github.com/hjs-spec/jep-core/blob/main/docs/REPOSITORY-CONSOLIDATION-2026-09.md) records the documentation move.
