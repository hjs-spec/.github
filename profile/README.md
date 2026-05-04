# HJS Spec

**JEP / HJS / JAC** — a layered protocol stack for verifiable judgment events, accountability receipts, and declared dependency chains in human, organizational, software, and AI-agent systems.

---

## Current Version Stack

| Layer | Current Draft | Current Implementation | Status |
|---|---|---|---|
| **JEP** | `draft-wang-jep-judgment-event-protocol-06` + Profiles + Conformance | [`jep-v06`](https://github.com/hjs-spec/jep-v06) | Current protocol core |
| **HJS** | `draft-wang-hjs-accountability-05` | [`hjs-05`](https://github.com/hjs-spec/hjs-05) | Current companion implementation seed |
| **JAC** | `draft-wang-jac-02` | [`jac-agent-02`](https://github.com/hjs-spec/jac-agent-02) | Current chain implementation seed |

---

## Public Drafts

- **JEP-Core**: https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/
- **JEP-Profiles**: https://datatracker.ietf.org/doc/draft-wang-jep-profiles/
- **JEP-Conformance**: https://datatracker.ietf.org/doc/draft-wang-jep-conformance/
- **HJS Accountability Receipts**: https://datatracker.ietf.org/doc/draft-wang-hjs-accountability/
- **JAC Declared Dependency Chains**: https://datatracker.ietf.org/doc/draft-wang-jac/

---

## Public Implementations and Resources

- **JEP v0.6 Repository**: https://github.com/hjs-spec/jep-v06
- **HJS v0.5 Repository**: https://github.com/hjs-spec/hjs-05
- **JAC v0.5 Repository**: https://github.com/hjs-spec/jac-agent-02
- **JEP v0.6 Spec Demo Space**: https://huggingface.co/spaces/yuqiangJEP/jep-v06-spec-demo/tree/main
- **JEP v0.6 Conformance Suite Dataset**: https://huggingface.co/datasets/yuqiangJEP/jep-v06-conformance-suite

---

## Architecture

The stack is intentionally layered.

```text
JEP = atomic signed judgment events
HJS = accountability receipts, archive/privacy/evidence lifecycle
JAC = declared dependency and accountability chains
````

### JEP

**Judgment Event Protocol** is the neutral narrow-waist event layer.

JEP defines signed, verifiable events for:

| Verb  | Name         | Meaning                                                           |
| ----- | ------------ | ----------------------------------------------------------------- |
| **J** | Judgment     | An actor made or endorsed a decision-related claim                |
| **D** | Delegation   | An actor delegated a task, authority, capability, or context      |
| **T** | Termination  | An actor terminated a delegation, authority, context, or reliance |
| **V** | Verification | An actor verified something within a declared scope               |

JEP-Core defines the stable event format, signatures, hashes, references, validation levels, failure codes, and extension framework.

JEP-Profiles define optional interoperability with DID/VC, X.509, OAuth/OIDC, RATS, Local IAM, HJS, JAC, blockchain anchors, and AI actor contexts.

JEP-Conformance defines schemas, signed vectors, invalid cases, reference validators, and conformance classes.

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

## Core Repositories

| Repository                                                 | Purpose                                                                                   |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| [`jep-v06`](https://github.com/hjs-spec/jep-v06)           | JEP v0.6 draft set, profiles, conformance suite, validators, and public resources         |
| [`hjs-05`](https://github.com/hjs-spec/hjs-05)             | HJS v0.5 implementation seed aligned with `draft-wang-hjs-accountability-05` and JEP v0.6 |
| [`jac-agent-02`](https://github.com/hjs-spec/jac-agent-02) | JAC v0.5 implementation seed aligned with `draft-wang-jac-02`, JEP v0.6, and HJS v0.5     |

---

## What This Stack Does

The JEP / HJS / JAC stack provides infrastructure for recording, exporting, validating, and composing judgment-related events.

It is designed to support:

* human accountability;
* organizational accountability;
* AI-agent behavior receipts;
* delegation and termination records;
* verification traces;
* archive and evidence lifecycle;
* declared dependency chains;
* cross-system interoperability.

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

---

## Version Boundary

Current public version line:

```text
JEP v0.6
HJS v0.5
JAC v0.5
```

Older repositories such as JEP v0.4, HJS v0.4, or early JAC demos should be treated as historical design artifacts unless explicitly marked current.

---

## Conformance and Testing

JEP v0.6 includes a public conformance suite:

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

Code, schemas, examples, validators, and test artifacts are provided under the license stated in each repository.

See individual repositories for implementation-specific licensing terms.

---

## Contact

* **Email**: [signal@humanjudgment.org](mailto:signal@humanjudgment.org)
* **Issues**: Use the issue tracker of the relevant repository.

```
```
