# Judgment Event Protocol ecosystem

JEP-Core-0.6 defines signed atomic Judgment, Delegation, Termination and Verification events (`J`, `D`, `T`, `V`). The API and language SDKs provide event creation and verification. HJS addresses archives, privacy, receipts and evidence lifecycle; JAC describes declared dependency chains over JEP/HJS. These layers do not automatically establish identity, authorization, truth or complete logging.

## Start here

| Repository | Current entry point |
|---|---|
| [jep-quickstart](https://github.com/hjs-spec/jep-quickstart) | Python SDK with a real local Core 0.6 API; simulated business tools |
| [jep-e2e-demo](https://github.com/hjs-spec/jep-e2e-demo) | Signed J/D/T/V creation and archival verification; command `jep-e2e` |
| [jep-api](https://github.com/hjs-spec/jep-api) | Core 0.6 API implementation, Level 1 syntax and cryptographic verification |
| [cli](https://github.com/hjs-spec/cli) | Standalone `jep` command; package `jep-cli` |
| [sdk-py](https://github.com/hjs-spec/sdk-py) | Python HTTP SDK; package `jep-sdk-py` |
| [sdk-js](https://github.com/hjs-spec/sdk-js) | JavaScript/TypeScript HTTP SDK; GitHub tarball available, npm publication paused |
| [sdk-go](https://github.com/hjs-spec/sdk-go) | Go HTTP SDK |

Follow the local setup in the quickstart README. The protocol profile is `jep-core-0.6` and wire version is `"1"`; software release numbers are separate. Current code releases do not update the live API or Hugging Face Space. Archival verification through these examples reports Level 1, not authority or dependency-chain validation.

## Protocol boundaries

| Repository | Responsibility |
|---|---|
| [jep-v06](https://github.com/hjs-spec/jep-v06) | Normative Core baseline, profiles, conformance inputs and delivery evidence |
| [hjs-05](https://github.com/hjs-spec/hjs-05) | Archive, privacy, receipt and evidence lifecycle |
| [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) | Declared dependencies, including `ext["https://jac.org/chain"]` |
| [jep-architecture](https://github.com/hjs-spec/jep-architecture) | Layer responsibilities and verification boundaries |

JEP has its own canonicalization, signature and event-hash rules. Application envelopes may add sequence and hash-link metadata outside the signed Core object. Such metadata is not a new Core field, an HJS receipt or a JAC declaration. JAC declarations do not by themselves prove real causality or valid authority.

## Runtime integrations

| Repository | Purpose |
|---|---|
| [jep-runtime](https://github.com/hjs-spec/jep-runtime) | Local runtime envelope and replay semantics; command `jep-runtime` |
| [jep-langgraph-adapter](https://github.com/hjs-spec/jep-langgraph-adapter) | LangGraph integration |
| [jep-openai-agents-middleware](https://github.com/hjs-spec/jep-openai-agents-middleware) | OpenAI Agents integration |
| [jep-mcp-wrapper](https://github.com/hjs-spec/jep-mcp-wrapper) | MCP integration |
| [jep-github-action](https://github.com/hjs-spec/jep-github-action) | CI integration |
| [jep-authority-runtime](https://github.com/hjs-spec/jep-authority-runtime) | Application authority and replay checks |
| [jep-replay-visualizer](https://github.com/hjs-spec/jep-replay-visualizer) | Archive visualization |
| [jep-lineage-explorer](https://github.com/hjs-spec/jep-lineage-explorer) | Declared lineage exploration |

Each runtime has its own supported envelope and verification scope; a successful local replay is not a blanket Core/HJS/JAC conformance result. Consult the repository's format and migration notes before mixing archives.

## Historical and experimental work

| Repository | Status |
|---|---|
| [jep-agent-sdk](https://github.com/hjs-spec/jep-agent-sdk) | Historical JEP-04/JAC-01 format; import `jep_agent`, command `jep-agent` |
| [aip-judgment-sidecar](https://github.com/hjs-spec/aip-judgment-sidecar) | Independent signed receipt prototype; no policy evaluator means undetermined |
| [Agent-Blackbox](https://github.com/hjs-spec/Agent-Blackbox) | Experimental incident reconstruction |
| [jep-vs-logging](https://github.com/hjs-spec/jep-vs-logging) | Local hash-envelope illustration, not Core conformance |
| [jep-papers-and-corpus](https://github.com/hjs-spec/jep-papers-and-corpus) | Research materials |
| [JEP-EU-AI-Act-Mapping-Notes](https://github.com/hjs-spec/JEP-EU-AI-Act-Mapping-Notes) | Exploratory mapping notes |
| [whitepaper](https://github.com/hjs-spec/whitepaper) | Conceptual materials |

Old mocks and frozen comparison baselines retain their historical formats. They are not silently migrated into current protocol evidence.

## Public resources

- [JEP draft](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/), [profiles](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/), [conformance](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/)
- [HJS draft](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/), [JAC draft](https://datatracker.ietf.org/doc/draft-wang-jac/)
- [Hugging Face spec demo](https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo), [conformance dataset](https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite)

Signatures support cryptographic integrity under the selected trust policy. They do not establish factual correctness, legal liability, regulatory compliance or completeness. Report implementation issues in the relevant repository.

Contact: [signal@humanjudgment.org](mailto:signal@humanjudgment.org).
