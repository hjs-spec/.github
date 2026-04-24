# JEP Protocol

**Judgment Event Protocol** — a minimal, portable protocol for recording, transferring, and verifying responsibility in AI systems.

IETF Internet-Draft: draft-wang-jep-judgment-event-protocol-04

---

## What This Is

JEP provides cryptographic receipts for AI decisions. Four immutable primitives define every event. No more, no less.

The protocol is designed to be:
- **Minimal** — Four verbs cover all decision-related operations
- **Portable** — Cryptographic receipts work across heterogeneous platforms
- **Verifiable** — Third-party validation without pre-established trust
- **Privacy-preserving** — No personal data collection at the protocol layer

---

## The Four Core Primitives

| Primitive | Description |
|-----------|-------------|
| **J (Judge)** | Record a decision: who, what, when, context |
| **D (Delegate)** | Transfer authority with scope and expiry |
| **T (Terminate)** | End a responsibility chain |
| **V (Verify)** | Validate record integrity and chain continuity |

These primitives are immutable. Extensions may add fields, but the core grammar does not change.

---

## Core Repositories

| Repository | Description | Language | License |
|------------|-------------|----------|---------|
| `spec` | Protocol specification | Markdown | CC0 1.0 |
| `core` | Reference implementation | Rust | Apache 2.0 |
| `api` | Hosted API service | Node.js | MIT |
| `sdk-py` | Python SDK | Python | MIT |
| `sdk-js` | JavaScript SDK | JavaScript | MIT |
| `cli` | Command-line tool | Node.js | MIT |
| `whitepaper` | AI Judgment Layer White Paper | PDF | CC0 1.0 |

---

## Quick Start

### Python

```python
from jep import JEPClient

client = JEPClient(api_key="your-key")
result = client.judgment("user@example.com", "approve")
print(result['id'])  # jgd_1234567890abcd
```

### JavaScript

```javascript
import JEPClient from '@jep/sdk-js';

const client = new JEPClient({ apiKey: 'your-key' });
const result = await client.judgment({
  entity: 'user@example.com',
  action: 'approve'
});
console.log(result.id);  // jgd_1234567890abcd
```

### CLI

```bash
jep judgment create --entity user@example.com --action approve
```

### Rust

```rust
use jep_core::JudgmentEvent;

let event = JudgmentEvent::new("user@example.com", "approve");
let receipt = event.sign()?;
assert!(receipt.verify()?);
```

---

## What JEP Does Not Do

- Does not assign legal liability or culpability
- Does not enforce monitoring or governance hierarchies
- Does not provide encryption — transport security is the deployer's responsibility
- Does not store plaintext personal data

JEP is a neutral recording layer. It records objective events without judging legality, intent, or fault.

---

## Contact

- **Email**: signal@humanjudgment.org
- **Issues**: Use individual repository issue trackers

---

## License

- **Protocol Specification**: MIT or Apache 2.0
- **Code Implementations**: MIT or Apache 2.0 (see individual repositories)
