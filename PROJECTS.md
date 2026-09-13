# Project and resource index

For the protocol, SDKs, API, and a local quickstart, start at the [organization homepage](https://github.com/hjs-spec). This index covers additional integrations and materials; inclusion does not imply the same format or verification support across projects.

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

## Companion implementation boundaries

- [HJS](https://github.com/hjs-spec/hjs-05): receipts bind metadata to event hashes. Receipt validation alone does not verify event signatures, durable retention, or enforcement of a privacy policy.
- [JAC](https://github.com/hjs-spec/jac-agent-02): declaration and fragment-hash checks do not authenticate referenced parents or establish real-world causality or complete logging.

Companion extensions preserve JEP-Core's event, signature, and hash semantics. Critical extensions require a verifier that implements their semantics. Stronger guarantees require the corresponding profiles, evidence, trust configuration, and validation logic.

## Research, experiments, and historical implementations

| Resource | Scope |
|---|---|
| [Whitepaper](https://github.com/hjs-spec/whitepaper) | Conceptual architecture and historical development |
| [Papers and corpus](https://github.com/hjs-spec/jep-papers-and-corpus) | Research materials and exploratory scenarios |
| [Agent SDK](https://github.com/hjs-spec/jep-agent-sdk) | Historical JEP-04/JAC-01 implementation, distinct from the current language SDKs |
| [Judgment Sidecar](https://github.com/hjs-spec/aip-judgment-sidecar) | Independent signed-receipt prototype |
| [Agent Blackbox](https://github.com/hjs-spec/Agent-Blackbox) | Experimental incident reconstruction |

Historical signed records, examples, and frozen comparison baselines retain their original formats. Follow explicit compatibility instructions when reading them.

## Drafts and public resources

- **JEP drafts:** [Core](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/) · [Profiles](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/) · [Conformance](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/)
- **Companion drafts:** [HJS](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/) · [JAC](https://datatracker.ietf.org/doc/draft-wang-jac/)
- **Hugging Face:** [Specification demo](https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo) · [Conformance dataset](https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite)

Hosted resources may lag repository changes; check their revision before using them as implementation evidence. Current delivery status is linked from the organization homepage.
