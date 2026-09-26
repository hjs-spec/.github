# Project directory

Use the [four starting points](https://github.com/hjs-spec) first. This directory is the single organization-wide navigation index; protocol definitions stay in **jep-core**, and examples must identify their actual format.

## Current Core 0.7 path

| Repository | Responsibility |
|---|---|
| [jep-core](https://github.com/hjs-spec/jep-core) | Normative source, frozen published drafts, current schemas/vectors and reference validator; explicit legacy tools |
| [jep-quickstart](https://github.com/hjs-spec/jep-quickstart) | Default local onboarding: real SDK/API signing and archival replay |
| [sdk-py](https://github.com/hjs-spec/sdk-py) | Python HTTP client |
| [sdk-js](https://github.com/hjs-spec/sdk-js) | JavaScript HTTP client; check Releases for downloadable tarballs and registry availability |
| [sdk-go](https://github.com/hjs-spec/sdk-go) | Go HTTP client |
| [jep-api](https://github.com/hjs-spec/jep-api) | Reference service, signing/storage providers and acceptance state |
| [cli](https://github.com/hjs-spec/cli) | Command-line HTTP client |
| [jep-agent-sdk](https://github.com/hjs-spec/jep-agent-sdk) | Local agent recorder, current event verification, adapters and reports; historical formats require explicit support |
| [Agent-Blackbox](https://github.com/hjs-spec/Agent-Blackbox) | Alpha trace recorder and incident review; fresh Core 0.7 events, explicit historical preservation |

Release numbers are software versions. They do not rename the protocol. Check a component's documented verification scope before combining it with another component.

## Companion implementations and integrations

These projects have their own envelopes, storage contracts or verification scopes. Inclusion here does not imply full Core 0.7, HJS or JAC conformance.

| Repository | Responsibility |
|---|---|
| [HJS draft](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/) | Archive/receipt/privacy companion; the owner confirmed deletion of `hjs-spec/hjs-05` on 2026-09-26; historical citations remain in release records |
| [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) | JAC declarations and fragment checks |
| [jep-runtime](https://github.com/hjs-spec/jep-runtime) | Local execution/replay envelope; signed Core wire events belong to SDK/API |
| [jep-langgraph-adapter](https://github.com/hjs-spec/jep-langgraph-adapter) | Runtime integration for LangGraph |
| [jep-openai-agents-middleware](https://github.com/hjs-spec/jep-openai-agents-middleware) | Runtime integration for OpenAI Agents |
| [jep-mcp-wrapper](https://github.com/hjs-spec/jep-mcp-wrapper) | Runtime integration for MCP |
| [jep-authority-runtime](https://github.com/hjs-spec/jep-authority-runtime) | Application authority checks and explicit policy |
| [jep-github-action](https://github.com/hjs-spec/jep-github-action) | Existing action and its explicitly versioned validation contract |
| [aip-judgment-sidecar](https://github.com/hjs-spec/aip-judgment-sidecar) | Independent signed-receipt experiment |
| [shutup-mcp](https://github.com/hjs-spec/shutup-mcp) | Independent experimental MCP tool |

Receipt validation alone does not authenticate event signatures or prove retention. Declared dependency checks do not prove causality or completeness. Unsupported critical extensions must not be silently treated as understood.

## Tools, explanations and preserved baselines

| Repository | Responsibility |
|---|---|
| [jep-replay-visualizer](https://github.com/hjs-spec/jep-replay-visualizer) | Archive visualization; consult supported envelope formats |
| [jep-lineage-explorer](https://github.com/hjs-spec/jep-lineage-explorer) | Declared lineage visualization |
| [jep-claude-replay](https://github.com/hjs-spec/jep-claude-replay) | Specific replay integration |
| [Architecture in Core](https://github.com/hjs-spec/jep-core/tree/main/docs/architecture) | Maintained explanatory diagrams; [old repository](https://github.com/hjs-spec/jep-architecture) retired to historical links |
| [Logging comparison in Core](https://github.com/hjs-spec/jep-core/blob/main/docs/comparisons/logging.md) | Maintained explanation and preserved unsigned example; [old repository](https://github.com/hjs-spec/jep-vs-logging) retired |
| [jep-e2e-demo](https://github.com/hjs-spec/jep-e2e-demo) | Retired Core 0.6 demonstration with preserved releases; use Quickstart for current onboarding |
| [jep-hjs-odr-boundary-test-01](https://github.com/hjs-spec/jep-hjs-odr-boundary-test-01) | Frozen comparison/evidence baseline |
| [whitepaper](https://github.com/hjs-spec/whitepaper) | Conceptual and historical materials |
| [jep-papers-and-corpus](https://github.com/hjs-spec/jep-papers-and-corpus) | Research and corpus materials |
| [.github](https://github.com/hjs-spec/.github) | Organization homepage and this directory |

The [consolidation record](https://github.com/hjs-spec/jep-core/blob/main/docs/REPOSITORY-CONSOLIDATION-2026-09.md) records source revisions and the distinction between retired maintenance and GitHub's archive setting. The [portable evidence decision](https://github.com/hjs-spec/jep-core/blob/main/docs/decisions/portable-evidence-repository.md) explains why no extra credential repository is created yet.

## Maintenance rules

- Keep one current onboarding path; link to it rather than copying another quickstart.
- Keep protocol definitions, schemas and conformance vectors in jep-core. Downstream copies identify their source revision.
- Keep package releases independent where public imports, commands or dependencies differ. Avoid repository renames or mergers that break existing consumers.
- Absorb useful pending changes, then close superseded PRs. Do not merge obsolete version rollbacks or duplicate validators merely to clear the queue.
- Publish new immutable versions for changed software. Verify VERSION, package metadata and built artifacts agree; workflow edits alone must not trigger a new release.
- Preserve published drafts, historical signatures and frozen baselines. A new protocol revision is separate from a software repair release.

## Public drafts

[JEP Core](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/) · [Profiles](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/) · [Conformance](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/) · [HJS](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/) · [JAC](https://datatracker.ietf.org/doc/draft-wang-jac/)
