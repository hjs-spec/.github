# Judgment Event Protocol (JEP)

**A neutral event protocol for recording and verifying judgment-related acts across human, organizational, software, and AI-agent systems.**

JEP defines a common signed event format for four primitives: **Judgment, Delegation, Termination, and Verification** (`J`, `D`, `T`, `V`).

It enables independent systems to exchange judgment-event records and check their structure and signatures under explicit validation rules.

This organization hosts the protocol drafts, reference validators, SDKs, integrations, and companion implementations.

## Start here

| Your goal | Entry point |
|---|---|
| Understand the protocol | [JEP-Core-0.6 specification](https://github.com/hjs-spec/jep-v06) |
| Run a working example | [Local quickstart](https://github.com/hjs-spec/jep-quickstart) · [End-to-end demo](https://github.com/hjs-spec/jep-e2e-demo) |
| Integrate with your application | [Python SDK](https://github.com/hjs-spec/sdk-py) · [JavaScript / TypeScript SDK](https://github.com/hjs-spec/sdk-js) · [Go SDK](https://github.com/hjs-spec/sdk-go) |
| Check conformance and implementation evidence | [Validators and test vectors](https://github.com/hjs-spec/jep-v06#conformance-implementations) · [Release and verification record](https://github.com/hjs-spec/jep-v06/blob/main/docs/RELEASE-DELIVERY-2026-09.md) |

For event creation and verification, see the [API implementation](https://github.com/hjs-spec/jep-api) and [command-line client](https://github.com/hjs-spec/cli).

## Protocol layers

| Layer | Responsibility | Repository |
|---|---|---|
| **JEP** | Atomic signed Judgment, Delegation, Termination, and Verification events | [jep-v06](https://github.com/hjs-spec/jep-v06) |
| **HJS** | Archive receipts, privacy and evidence-lifecycle metadata | [hjs-05](https://github.com/hjs-spec/hjs-05) |
| **JAC** | Declared dependencies between JEP events and HJS objects | [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) |

HJS and JAC are companion layers. Their extensions and profiles preserve JEP-Core's event, signature, and hash semantics.

See the [architecture overview](https://github.com/hjs-spec/jep-architecture) for the relationship between protocol layers, runtime integrations, and applications.

## Implementation status

- **Protocol baseline:** JEP-Core-0.6, with wire version `"jep": "1"`. Software release numbers are versioned separately.
- **Local use:** The quickstart runs against a real local API. Python, JavaScript / TypeScript, and Go SDKs provide API clients.
- **Verification:** The API provides Level 1 structure and cryptographic verification. Reference validators support additional checks as documented in their implementations.
- **Distribution:** The JavaScript SDK is available as a GitHub release tarball; npm publication is paused.
- **Hosted services:** Live API and Hugging Face deployment remain deferred. Use the documented local setup to evaluate the current implementation.

Published versions, interoperability checks, migration notes, and delivery status are recorded in the [release and verification record](https://github.com/hjs-spec/jep-v06/blob/main/docs/RELEASE-DELIVERY-2026-09.md).

## Verification boundaries

Results report only the checks actually completed. A valid signature supports cryptographic integrity under the selected trust configuration; it does not by itself establish actor identity, valid authorization, factual truth, legal liability, or complete logging.

HJS receipt metadata does not prove durable retention or enforcement of a privacy policy. JAC declaration validation does not authenticate referenced parents or prove real-world causality. Critical extensions require a verifier that implements their semantics.

Applications requiring stronger guarantees must supply the corresponding profiles, evidence, trust configuration, and validation logic.

## Runtime integrations and tools

| Integration or task | Repository |
|---|---|
| LangGraph | [jep-langgraph-adapter](https://github.com/hjs-spec/jep-langgraph-adapter) |
| OpenAI Agents | [jep-openai-agents-middleware](https://github.com/hjs-spec/jep-openai-agents-middleware) |
| Model Context Protocol | [jep-mcp-wrapper](https://github.com/hjs-spec/jep-mcp-wrapper) |
| GitHub Actions | [jep-github-action](https://github.com/hjs-spec/jep-github-action) |
| Runtime envelopes and replay | [jep-runtime](https://github.com/hjs-spec/jep-runtime) |
| Application authority checks | [jep-authority-runtime](https://github.com/hjs-spec/jep-authority-runtime) |
| Archive visualization | [jep-replay-visualizer](https://github.com/hjs-spec/jep-replay-visualizer) |
| Declared lineage exploration | [jep-lineage-explorer](https://github.com/hjs-spec/jep-lineage-explorer) |

Consult each repository's supported formats, verification scope, and migration instructions before combining integrations or replaying existing archives.

## Research and historical work

- [Whitepaper](https://github.com/hjs-spec/whitepaper) — conceptual architecture and historical development.
- [Papers and corpus](https://github.com/hjs-spec/jep-papers-and-corpus) — research materials and exploratory scenarios.
- [Agent SDK](https://github.com/hjs-spec/jep-agent-sdk) — historical JEP-04/JAC-01 implementation, distinct from the current language SDKs.
- [Judgment Sidecar](https://github.com/hjs-spec/aip-judgment-sidecar) — independent signed-receipt prototype.
- [Agent Blackbox](https://github.com/hjs-spec/Agent-Blackbox) — experimental incident reconstruction.

Historical signed records, examples, and frozen comparison baselines retain their original formats.

## Drafts and public resources

- **JEP:** [Core](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/) · [Profiles](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/) · [Conformance](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/)
- **Companions:** [HJS](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/) · [JAC](https://datatracker.ietf.org/doc/draft-wang-jac/)
- **Hugging Face:** [Specification demo](https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo) · [Conformance dataset](https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite)

## Contributing and contact

Report implementation issues in the relevant repository. For interoperability reports, include the implementation version, selected validation profile, test input, and observed result.

Contact: [signal@humanjudgment.org](mailto:signal@humanjudgment.org)
