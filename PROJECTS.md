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

Local acceptance is single-process. For acceptance across hosts, use the API with [shared PostgreSQL state](https://github.com/hjs-spec/jep-api/blob/main/DEPLOYMENT.md#multiple-hosts).

<a id="optional-components"></a>
<a id="optional-protocol-companions"></a>

## Optional tools

Use these for incident review or declared dependency fragments. Their supported
formats and checks are listed in the [format matrix](https://github.com/hjs-spec/jep-core/blob/main/docs/architecture/architecture-notes.md#format-and-verification-matrix).

| Repository | Purpose / boundary |
|---|---|
| [Agent-Blackbox](https://github.com/hjs-spec/Agent-Blackbox) | Alpha incident recorder; local evidence digests, declared links and integrity checks |
| [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) | JAC declarations and fragment checks; pinned historical demo events |

## Research and organization

| Repository | Responsibility |
|---|---|
| [whitepaper](https://github.com/hjs-spec/whitepaper) | Original conceptual paper; published body preserved |
| [jep-papers-and-corpus](https://github.com/hjs-spec/jep-papers-and-corpus) | Versioned research and exploratory corpus; not a conformance suite |
| [.github](https://github.com/hjs-spec/.github) | Organization homepage, this directory and delivery records |

[Interoperability checks](https://github.com/hjs-spec/jep-core/tree/main/integration#current-core-07--binding02) · [Released components](DELIVERY-CURRENT.md)

<a id="historical-workflow-integration"></a>
<a id="retired-experiments"></a>
<a id="earlier-documentation-archives"></a>

## Archives

[Archived repositories and migration references](ARCHIVES.md).
