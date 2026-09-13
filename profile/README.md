# Judgment Event Protocol (JEP)

A signed event format for recording **Judgment, Delegation, Termination, and Verification** (`J`, `D`, `T`, `V`) across human, organizational, software, and AI-agent systems.

## Start here

| Your goal | Entry point |
|---|---|
| Understand the protocol | [JEP-Core-0.6 specification](https://github.com/hjs-spec/jep-v06) |
| Run an example | [Local quickstart](https://github.com/hjs-spec/jep-quickstart) · [End-to-end demo](https://github.com/hjs-spec/jep-e2e-demo) |
| Integrate an application | [Python](https://github.com/hjs-spec/sdk-py) · [JavaScript / TypeScript](https://github.com/hjs-spec/sdk-js) · [Go](https://github.com/hjs-spec/sdk-go) · [API](https://github.com/hjs-spec/jep-api) · [CLI](https://github.com/hjs-spec/cli) |
| Check implementation evidence | [Validators and test vectors](https://github.com/hjs-spec/jep-v06#conformance-implementations) · [Release and verification record](https://github.com/hjs-spec/jep-v06/blob/main/docs/RELEASE-DELIVERY-2026-09.md) |

**Current baseline:** JEP-Core-0.6, wire version `"jep": "1"`; software versions are separate. The API provides Level 1 structure and cryptographic verification. Use the local setup to evaluate current code. The JavaScript SDK is distributed through a GitHub release tarball; npm publication and hosted API/Hugging Face updates remain deferred.

## Companion layers and other projects

[HJS](https://github.com/hjs-spec/hjs-05) provides archive receipts and privacy/lifecycle metadata. [JAC](https://github.com/hjs-spec/jac-agent-02) records declared dependencies. See the [architecture overview](https://github.com/hjs-spec/jep-architecture) for their relationship to JEP.

The [project and resource index](https://github.com/hjs-spec/.github/blob/main/PROJECTS.md) lists runtime integrations, research, historical implementations, public drafts, and Hugging Face resources.

## Verification scope

Results describe completed checks under the selected trust configuration. Signature validity alone does not establish identity, authorization, truth, legal liability, or complete logging. HJS metadata does not prove durable retention; JAC declarations do not prove causality. See each implementation's validation scope before relying on its results.

For interoperability reports, include the implementation version, validation profile, input, and observed result in the relevant repository's issue tracker.

Contact: [signal@humanjudgment.org](mailto:signal@humanjudgment.org)
