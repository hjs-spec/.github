# JEP Runtime Stack

Portable, replayable, and verifiable accountability runtime for AI agents, tools, workflows, delegation systems, and cross-runtime execution environments.

JEP / HJS / JAC is a layered protocol and runtime stack for:

* replayable judgment events
* verifiable delegation lineage
* portable accountability receipts
* dependency-chain reconstruction
* authority propagation semantics
* cross-system accountability interoperability

The stack acts as a neutral narrow-waist accountability layer between:

```text id="1ffr5w"
Human / Organization Intent
              ↓
        Agent Runtime
              ↓
      Tool / Workflow Execution
              ↓
      Delegation Propagation
              ↓
      Verification and Replay
```

---

# Start Here

## New Developers

| Repository                                                   | Purpose                                   |
| ------------------------------------------------------------ | ----------------------------------------- |
| [jep-quickstart](https://github.com/hjs-spec/jep-quickstart) | Five-minute developer onboarding          |
| [jep-e2e-demo](https://github.com/hjs-spec/jep-e2e-demo)     | End-to-end replayable accountability demo |

---

## Runtime Core

| Repository                                             | Purpose                                     |
| ------------------------------------------------------ | ------------------------------------------- |
| [jep-runtime](https://github.com/hjs-spec/jep-runtime) | Executable accountability runtime           |
| [jep-api](https://github.com/hjs-spec/jep-api)         | Event creation and verification runtime API |
| [jep-cli](https://github.com/hjs-spec/jep-cli)         | CLI tooling for replay and verification     |
| [jep-sdk-py](https://github.com/hjs-spec/jep-sdk-py)   | Python SDK                                  |
| [jep-sdk-js](https://github.com/hjs-spec/jep-sdk-js)   | JavaScript SDK                              |
| [jep-sdk-go](https://github.com/hjs-spec/jep-sdk-go)   | Go SDK                                      |

---

## Protocol Core

| Repository                                               | Purpose                                             |
| -------------------------------------------------------- | --------------------------------------------------- |
| [jep-v06](https://github.com/hjs-spec/jep-v06)           | JEP v0.6 protocol core                              |
| [hjs-05](https://github.com/hjs-spec/hjs-05)             | Accountability receipt and evidence lifecycle layer |
| [jac-agent-02](https://github.com/hjs-spec/jac-agent-02) | Delegation and dependency-chain reconstruction      |

---

## Runtime Integrations

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
* execution replay reconstruction

---

# Replay and Observability

| Repository                                                                 | Purpose                                         |
| -------------------------------------------------------------------------- | ----------------------------------------------- |
| [jep-replay-visualizer](https://github.com/hjs-spec/jep-replay-visualizer) | Replay and visualize accountability lineage     |
| [jep-lineage-explorer](https://github.com/hjs-spec/jep-lineage-explorer)   | Explore delegation propagation and ancestry     |
| [jep-authority-runtime](https://github.com/hjs-spec/jep-authority-runtime) | Authority propagation and replay runtime        |
| [Agent-Blackbox](https://github.com/hjs-spec/Agent-Blackbox)               | Experimental replay and incident reconstruction |

---

# Runtime Architecture

```text id="r5u5kp"
Human / Organization
        ↓
Agent Runtime
        ↓
JEP Runtime Middleware
        ↓
Judgment / Delegation Events
        ↓
HJS Accountability Receipts
        ↓
JAC Dependency and Lineage Graph
        ↓
Archive + Replay Verification
```

---

# End-to-End Execution Flow

```text id="y5gr88"
Human
  ↓
OpenAI Agent
  ↓
MCP Tool Execution
  ↓
JEP Judgment Event
  ↓
HJS Accountability Receipt
  ↓
JAC Delegation Chain
  ↓
Archive Storage
  ↓
Replay Verification
```

---

# Why This Exists

As AI systems become increasingly autonomous, accountability becomes a runtime problem.

Modern AI systems increasingly involve:

* multi-agent delegation
* tool execution
* workflow orchestration
* cross-runtime automation
* autonomous task propagation
* delegated authority chains
* replay-sensitive execution semantics

Without portable accountability semantics:

* delegation chains become opaque
* authority propagation becomes unverifiable
* replay and audit become fragmented
* cross-agent responsibility becomes non-portable
* runtime lineage becomes difficult to reconstruct

JEP Runtime Stack provides a replayable accountability execution layer for AI systems.

---

# What Makes JEP Different

JEP is NOT ordinary logging.

Traditional logging records events.

JEP Runtime provides:

* replayable accountability semantics
* delegation lineage reconstruction
* authority propagation tracking
* portable verification
* replay-safe execution traces
* cross-runtime accountability interoperability

JEP events are:

* canonicalized
* hash-linked
* replay-verifiable
* delegation-aware
* portability-oriented

The stack is designed for accountability replay, not just event storage.

---

# Quickstart

## Install

```bash id="pmy1zb"
pip install jep-runtime
```

---

## Minimal Example

```python id="rwl3tx"
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

```bash id="uhffgf"
jep replay archive.jsonl
```

Verification includes:

* delegation lineage
* event hash continuity
* authority propagation
* verification chains
* tamper detection
* replay integrity validation

---

# Stack Overview

```text id="n8rbw9"
JEP      = atomic signed judgment events
JEP API  = event creation and verification runtime
HJS      = accountability receipts and evidence lifecycle
JAC      = declared dependency and delegation lineage
Runtime  = executable accountability semantics
SDKs     = developer integration surface
Adapters = runtime insertion into agent ecosystems
Replay   = accountability reconstruction and verification
```

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

# Experimental and Research Repositories

| Repository                                                                             | Purpose                                           |
| -------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [jep-vs-logging](https://github.com/hjs-spec/jep-vs-logging)                           | Explains replayable accountability semantics      |
| [jep-architecture](https://github.com/hjs-spec/jep-architecture)                       | Runtime architecture diagrams and execution flows |
| [shutup-mcp](https://github.com/hjs-spec/shutup-mcp)                                   | Experimental MCP filtering proxy                  |
| [jep-papers-and-corpus](https://github.com/hjs-spec/jep-papers-and-corpus)             | Research papers and exploratory scenario corpus   |
| [JEP-EU-AI-Act-Mapping-Notes](https://github.com/hjs-spec/JEP-EU-AI-Act-Mapping-Notes) | Exploratory EU AI Act mapping notes               |
| [aip-judgment-sidecar](https://github.com/hjs-spec/aip-judgment-sidecar)               | Experimental sidecar runtime                      |
| [whitepaper](https://github.com/hjs-spec/whitepaper)                                   | Whitepapers and conceptual materials              |

Historical repositories (v0.4 lines and early demos) should be treated as historical design artifacts unless explicitly marked current.

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
* replay verification
* authority propagation semantics

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

# Design Principles

The stack is intentionally:

* protocol-minimal
* runtime-portable
* identity-neutral
* credential-neutral
* replay-oriented
* interoperability-first
* accountability-focused
* execution-path aware

---

# Contact

* Email: [signal@humanjudgment.org](mailto:signal@humanjudgment.org)
* Issues: use the issue tracker of the relevant repository
