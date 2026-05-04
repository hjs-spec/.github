# HJS Spec

**JEP / HJS / JAC** is a layered protocol stack for recording, verifying, exporting, and composing judgment-related events across human, organizational, software, and AI-agent systems.

The current public version line is:

```text
JEP v0.6
JEP API v0.6
HJS v0.5
JAC v0.5
````

---

## What This Is

This organization maintains the current public implementation and supporting materials for:

* **JEP** — Judgment Event Protocol: atomic signed judgment events;
* **HJS** — accountability receipts, archive metadata, privacy, and evidence lifecycle;
* **JAC** — declared dependency chains and accountability-path reconstruction;
* **JEP API / SDKs / CLI** — implementation seeds for creating and verifying JEP-Core events.

The stack is intentionally narrow and layered:

```text
JEP      = atomic signed judgment events
JEP API  = API seed for creating and verifying JEP-Core events
HJS      = accountability receipts and evidence lifecycle
JAC      = declared dependency and accountability chains
SDKs/CLI = developer access to the JEP API
```

---

## Current Canonical Repositories

| Repository                                                 | Role                                                                              | Status                  |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------- |
| [`jep-v06`](https://github.com/hjs-spec/jep-v06)           | JEP v0.6 draft set, profiles, conformance suite, validators, and public resources | Current protocol core   |
| [`jep-api`](https://github.com/hjs-spec/jep-api)           | FastAPI implementation seed for creating and verifying JEP-Core events            | Current API seed        |
| [`jep-sdk-py`](https://github.com/hjs-spec/jep-sdk-py)     | Python SDK for the JEP v0.6 API                                                   | Current SDK seed        |
| [`jep-sdk-js`](https://github.com/hjs-spec/jep-sdk-js)     | JavaScript SDK for the JEP v0.6 API                                               | Current SDK seed        |
| [`jep-sdk-go`](https://github.com/hjs-spec/jep-sdk-go)     | Go SDK for the JEP v0.6 API                                                       | Current SDK seed        |
| [`jep-cli`](https://github.com/hjs-spec/jep-cli)           | CLI for creating and verifying JEP v0.6 events                                    | Current CLI seed        |
| [`hjs-05`](https://github.com/hjs-spec/hjs-05)             | HJS v0.5 implementation seed aligned with JEP v0.6                                | Current companion layer |
| [`jac-agent-02`](https://github.com/hjs-spec/jac-agent-02) | JAC v0.5 implementation seed aligned with JEP v0.6 and HJS v0.5                   | Current chain layer     |

---

## Public Drafts

| Draft                              | Link                                                                                                                                                 |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JEP-Core**                       | [https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/) |
| **JEP-Profiles**                   | [https://datatracker.ietf.org/doc/draft-wang-jep-profiles/](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/)                               |
| **JEP-Conformance**                | [https://datatracker.ietf.org/doc/draft-wang-jep-conformance/](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/)                         |
| **HJS Accountability Receipts**    | [https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/](https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/)                   |
| **JAC Declared Dependency Chains** | [https://datatracker.ietf.org/doc/draft-wang-jac/](https://datatracker.ietf.org/doc/draft-wang-jac/)                                                 |

---

## Public Resources

| Resource                           | Link                                                                                                                                         |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| JEP v0.6 Spec Demo Space           | [https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo/tree/main](https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo/tree/main) |
| JEP v0.6 Conformance Suite Dataset | [https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite](https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite) |

---

## Experimental and Supporting Repositories

These repositories are useful, but they are not the normative protocol core.

| Repository              | Role                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| `jep-github-action`     | GitHub workflow integration seed for generating JEP v0.6 event artifacts                   |
| `Agent-Blackbox`        | Experimental agent trace recorder for JEP/HJS/JAC incident review and chain reconstruction |
| `shutup-mcp`            | Experimental MCP tool-list filtering proxy                                                 |
| `jep-papers-and-corpus` | Research papers and exploratory scenario corpus                                            |
| `jep-eu-compliance`     | Exploratory EU AI Act mapping notes for JEP; not legal advice                              |

Historical repositories such as JEP v0.4, HJS v0.4, early JAC demos, or early `spec` repositories should be treated as historical design artifacts unless explicitly marked current.

---

## Architecture

### JEP

**Judgment Event Protocol** is the neutral narrow-waist event layer.

JEP defines signed, verifiable events for:

| Verb  | Name         | Meaning                                                           |
| ----- | ------------ | ----------------------------------------------------------------- |
| **J** | Judgment     | An actor made or endorsed a decision-related claim                |
| **D** | Delegation   | An actor delegated a task, authority, capability, or context      |
| **T** | Termination  | An actor terminated a delegation, authority, context, or reliance |
| **V** | Verification | An actor verified something within a declared scope               |

JEP-Core defines the event format, signatures, hashes, references, validation levels, failure codes, and extension framework.

JEP-Profiles define optional interoperability with DID/VC, X.509, OAuth/OIDC, RATS, Local IAM, HJS, JAC, blockchain anchors, and AI actor contexts.

JEP-Conformance defines schemas, signed vectors, invalid cases, reference validators, and conformance classes.

---

### JEP API

**JEP API** is a JEP v0.6 implementation seed.

It demonstrates:

* JEP-Core event creation;
* JEP-Core event verification;
* JEP-style event hashes;
* JEP-style validation results;
* Ed25519 signing and verification;
* detached JWS Compact Serialization shape;
* `ext` / `ext_crit`;
* TTL and digest-only privacy extensions.

JEP API does **not** define a new protocol.
It does **not** replace JEP-Core, JEP-Profiles, or JEP-Conformance.

---

### HJS

**HJS** is a JEP-compatible accountability receipt and evidence-lifecycle companion layer.

HJS handles:

* behavior records;
* receipt manifests;
* receipt bundles;
* evidence references;
* archive metadata;
* receipt time and archive time;
* redaction manifests;
* selective disclosure;
* privacy-preserving export.

HJS does **not** redefine JEP-Core verbs, signatures, event hashes, validation levels, or failure codes.

---

### JAC

**JAC** is a declared dependency chain companion layer over JEP and HJS.

JAC handles:

* declared dependency links;
* chain roots;
* declared breaks;
* causal edge metadata;
* delegation paths;
* verification paths;
* termination paths;
* observed-log assumptions;
* chain fragments.

JAC does **not** redefine JEP-Core event format, signature semantics, event hashes, validation levels, or extension processing.

---

## What This Stack Does

The JEP / HJS / JAC stack provides infrastructure for:

* recording judgment-related events;
* signing and verifying event artifacts;
* exporting accountability receipts;
* referencing evidence without exposing raw evidence;
* representing delegation, termination, and verification traces;
* reconstructing declared dependency chains;
* supporting cross-system interoperability;
* enabling SDK, CLI, API, and workflow integrations.

---

## What This Stack Does Not Do

This stack does **not** determine:

* external truth;
* legal liability;
* moral responsibility;
* regulatory compliance;
* authorization validity;
* complete-log availability;
* model correctness;
* factual causality.

A valid signature proves cryptographic integrity under a validation profile.
It does not prove that the underlying claim is true.

A valid JAC chain proves declared dependency structure.
It does not prove legal liability.

An HJS archive receipt proves receipt or archival metadata under a profile.
It does not prove complete logging or factual correctness.

The JEP API, SDKs, CLI, and integration tools are implementation seeds.
They do not define new protocol semantics and do not claim production-grade trust-profile coverage.

---

## Conformance and Testing

JEP v0.6 includes a public conformance suite with:

* JSON Schemas;
* signed Ed25519 / JWS / JCS vectors;
* invalid test cases;
* profile examples;
* canonicalization fixtures;
* Python reference validator;
* TypeScript validator seed;
* Go validator seed;
* conformance metadata.

Public dataset:

[https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite](https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite)

---

## Security and Privacy Principles

The stack follows these principles:

* protocol-layer data minimization;
* digest references instead of raw evidence where possible;
* explicit validation levels;
* explicit audience and trust context;
* no implicit legal or factual conclusions;
* no hidden governance hierarchy;
* optional privacy-preserving archival and selective disclosure;
* explicit critical extension handling.

---

## License and Legal Notice

Internet-Draft documents are provided under the IETF Trust Legal Provisions and BCP 78 / BCP 79.

Code, schemas, examples, validators, SDKs, CLI tools, and test artifacts are provided under the license stated in each repository.

See individual repositories for implementation-specific licensing terms.

---

## Contact

* **Email**: [signal@humanjudgment.org](mailto:signal@humanjudgment.org)
* **Issues**: Use the issue tracker of the relevant repository.
