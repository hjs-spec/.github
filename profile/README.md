# JEP Runtime Stack

Portable, replayable, and verifiable accountability runtime for AI agents, tools, workflows, and delegation systems.

JEP / HJS / JAC is a layered protocol and runtime stack for:

* replayable judgment events
* verifiable delegation lineage
* portable accountability receipts
* dependency-chain reconstruction
* cross-system accountability interoperability

The stack is designed as a neutral narrow-waist accountability layer between:

```text
AI intent
    ↓
agent execution
    ↓
tool invocation
    ↓
delegation propagation
    ↓
verification and replay
```

---

# Why This Exists

As AI systems become autonomous, accountability becomes a runtime problem.

Modern AI systems increasingly involve:

* multi-agent delegation
* tool execution
* workflow orchestration
* cross-system automation
* autonomous task propagation

Without portable accountability semantics:

* delegation chains become opaque
* authority propagation becomes unverifiable
* replay and audit become fragmented
* cross-agent responsibility becomes non-portable

JEP Runtime Stack provides a replayable accountability execution layer for AI systems.

---

# Stack Overview

```text
JEP      = atomic signed judgment events
JEP API  = event creation and verification runtime
HJS      = accountability receipts and evidence lifecycle
JAC      = declared dependency and delegation lineage
Runtime  = executable accountability semantics
SDKs     = developer integration surface
Adapters = runtime insertion into agent ecosystems
```

---

# Core Layers

| Layer      | Purpose                                        |
| ---------- | ---------------------------------------------- |
| JEP        | Signed and replayable judgment events          |
| HJS        | Accountability receipts and evidence lifecycle |
| JAC        | Delegation and dependency-chain reconstruction |
| Runtime    | Executable accountability semantics            |
| SDKs / CLI | Developer access and integration               |
| Adapters   | Runtime insertion into agent ecosystems        |

---

# Runtime Integrations

JEP Runtime integrates directly into AI execution paths.

| Runtime / System  | Repository                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------- |
| LangGraph         | [jep-langgraph-adapter](https://github.com/hjs-spec/jep-langgraph-adapter)               |
| OpenAI Agents SDK | [jep-openai-agents-middleware](https://github.com/hjs-spec/jep-openai-agents-middleware) |
| MCP Tool Runtime  | [jep-mcp-wrapper](https://github.com/hjs-spec/jep-mcp-wrapper)                           |
| GitHub Actions    | [jep-github-action](https://github.com/hjs-spec/jep-github-action)                       |

These integrations allow:

* replayable execution traces
* delegation lineage reconstruction
* verifiable accountability propagation
* runtime verification semantics

---

# Quickstart

## Install

```bash
pip install jep-runtime
```

---

## Minimal Example

```python
from jep_runtime import JEPMiddleware

runtime = JEPMiddleware()

@runtime.wrap_tool("search")
def search_tool(query):
    return f"search result for {query}"

result = search_tool("JEP Runtime")
```

This automatically produces:

* Judgment Events
* Delegation Events
* Verification metadata
* Replayable accountability chains

---

# Replay and Verification

Replayable accountability is a core design principle.

Any archive can be replayed and verified:

```bash
jep replay archive.jsonl
```

Verification includes:

* delegation lineage
* event hash continuity
* authority propagation
* verification chains
* tamper detection

---

# Current Canonical Repositories

| Repository                                               | Role                                | Status  |
| -------------------------------------------------------- | ----------------------------------- | ------- |
| [jep-v06](https://github.com/hjs-spec/jep-v06)           | JEP v0.6 protocol core              | Current |
| [jep-runtime](https://github.com/hjs-spec/jep-runtime)   | Executable accountability runtime   | Current |
| [jep-api](https://github.com/hjs-spec/jep-api)           | Event creation and verification API | Current |
| [sdk-py](https://github.com/hjs-spec/sdk-py)             | Python SDK                          | Current |
| [sdk-js](https://github.com/hjs-spec/sdk-js)             | JavaScript SDK                      | Current |
| [sdk-go](https://github.com/hjs-spec/sdk-go)             | Go SDK                              | Current |
| [cli](https://github.com/hjs-spec/cli)                   | CLI tooling                         | Current |
| [hjs-05](https://github.com/hjs-spec/hjs-05)             | Accountability receipt layer        | Current |
| [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) | Delegation and dependency chains    | Current |

---

# Runtime and Observability

| Repository                                                                 | Purpose                                     |
| -------------------------------------------------------------------------- | ------------------------------------------- |
| [jep-replay-visualizer](https://github.com/hjs-spec/jep-replay-visualizer) | Replay and visualize accountability lineage |
| [jep-lineage-explorer](https://github.com/hjs-spec/jep-lineage-explorer)   | Explore delegation propagation and ancestry |
| [agent-blackbox](https://github.com/hjs-spec/agent-blackbox)               | Experimental agent trace reconstruction     |

---

# Public Drafts

| Draft                 | Link                                                                                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| JEP-Core              | [https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/) |
| JEP-Profiles          | [https://datatracker.ietf.org/doc/draft-wang-jep-profiles/](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/)                               |
| JEP-Conformance       | [https://datatracker.ietf.org/doc/draft-wang-jep-conformance/](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/)                         |
| HJS Accountability    | [https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/)                   |
| JAC Dependency Chains | [https://datatracker.ietf.org/doc/draft-wang-jac/](https://datatracker.ietf.org/doc/draft-wang-jac/)                                                 |

---

# Public Resources

| Resource                           | Link                                                                                                                                         |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| JEP v0.6 Spec Demo Space           | [https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo/tree/main](https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo/tree/main) |
| JEP v0.6 Conformance Suite Dataset | [https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite](https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite) |

---

# What This Stack Provides

The JEP Runtime Stack provides infrastructure for:

* recording judgment-related events
* replayable delegation lineage
* portable accountability semantics
* verifiable event chains
* accountability receipts
* dependency reconstruction
* cross-system interoperability
* runtime accountability integration

---

# What This Stack Does NOT Provide

This stack does NOT determine:

* external truth
* legal liability
* moral responsibility
* regulatory compliance
* factual correctness
* authorization validity
* complete-log guarantees

A valid signature proves cryptographic integrity under a validation profile.

It does NOT prove that an underlying claim is true.

A valid delegation chain proves declared accountability structure.

It does NOT prove legal causality or liability.

---

# Security and Privacy Principles

The stack follows:

* protocol-layer data minimization
* replay-safe canonicalization
* explicit validation semantics
* optional privacy-preserving archival
* selective disclosure
* append-only accountability chains
* explicit trust and audience boundaries

---

# Conformance and Testing

JEP v0.6 includes:

* JSON Schemas
* signed vectors
* invalid test cases
* canonicalization fixtures
* replay validation
* conformance metadata
* Python / TypeScript / Go validator seeds

Public dataset:

[https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite](https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite)

---

# Experimental Repositories

| Repository                                                                             | Purpose                             |
| -------------------------------------------------------------------------------------- | ----------------------------------- |
| [shutup-mcp](https://github.com/hjs-spec/shutup-mcp)                                   | Experimental MCP filtering proxy    |
| [jep-papers-and-corpus](https://github.com/hjs-spec/jep-papers-and-corpus)             | Research papers and scenario corpus |
| [JEP-EU-AI-Act-Mapping-Notes](https://github.com/hjs-spec/JEP-EU-AI-Act-Mapping-Notes) | Exploratory EU AI Act mapping notes |
| [aip-judgment-sidecar](https://github.com/hjs-spec/aip-judgment-sidecar)               | Experimental sidecar runtime        |

Historical repositories (v0.4 lines and early demos) should be treated as historical design artifacts unless explicitly marked current.

---

# Design Principles

The stack is intentionally:

* protocol-minimal
* runtime-portable
* identity-neutral
* credential-neutral
* replay-oriented
* interoperability-first
* accountability-focused

---

# Contact

* Email: [signal@humanjudgment.org](mailto:signal@humanjudgment.org)
* Issues: use the issue tracker of the relevant repository
