# JEP Protocol

<p align="center">
    <a href="https://github.com/hjs-protocol">
        <img src="https://img.shields.io/badge/Organization-hjs--protocol-blue" alt="Organization">
    </a>
    <a href="https://datatracker.ietf.org/doc/draft-wang-hjs-judgment-event/">
        <img src="https://img.shields.io/badge/IETF-draft--wang--hjs--judgment--event--00-blue" alt="IETF Draft">
    </a>
    <a href="https://github.com/hjs-protocol/spec/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/Spec%20License-CC0_1.0-lightgrey" alt="Spec License">
    </a>
    <a href="mailto:signal@humanjudgment.org">
        <img src="https://img.shields.io/badge/Contact-signal%40humanjudgment.org-green" alt="Contact">
    </a>
</p>

---

**JEP (Judgment Event Protocol)** is a minimal, portable protocol for recording, transferring, and verifying responsibility in AI systems. It provides cryptographic receipts for AI decisions, enabling traceable accountability across heterogeneous platforms.

 IETF [`draft-wang-hjs-judgment-event-00`](https://datatracker.ietf.org/doc/draft-wang-hjs-judgment-event/).

## Core Repositories

| Repository | Description | Language | License |
|------------|-------------|----------|---------|
| [`spec`](https://github.com/hjs-protocol/spec) | Protocol specification | Markdown | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) |
| [`core`](https://github.com/hjs-protocol/core) | Reference implementation | Rust | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| [`api`](https://github.com/hjs-protocol/api) | Hosted API service | Node.js | [MIT](https://opensource.org/licenses/MIT) |
| [`sdk-py`](https://github.com/hjs-protocol/sdk-py) | Python SDK | Python | [MIT](https://opensource.org/licenses/MIT) |
| [`sdk-js`](https://github.com/hjs-protocol/sdk-js) | JavaScript SDK | JavaScript | [MIT](https://opensource.org/licenses/MIT) |
| [`cli`](https://github.com/hjs-protocol/cli) | Command-line tool | Node.js | [MIT](https://opensource.org/licenses/MIT) |
| [`whitepaper`](https://github.com/hjs-protocol/whitepaper) | AI Judgment Layer White Paper | PDF | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) |

## The Four Core Primitives

| Primitive | Description | IETF Draft Section |
|-----------|-------------|-------------------|
| **Judgment** | Record a decision (who, what, when, context) | [Section 3.2.1](https://datatracker.ietf.org/doc/draft-wang-hjs-judgment-event/#section-3.2.1) |
| **Delegation** | Transfer authority with scope and expiry | [Section 3.2.2](https://datatracker.ietf.org/doc/draft-wang-hjs-judgment-event/#section-3.2.2) |
| **Termination** | End responsibility chains | [Section 3.2.3](https://datatracker.ietf.org/doc/draft-wang-hjs-judgment-event/#section-3.2.3) |
| **Verification** | Validate record integrity and chains | [Section 3.2.4](https://datatracker.ietf.org/doc/draft-wang-hjs-judgment-event/#section-3.2.4) |

## Quick Start

### Python
```python
from hjs import HJSClient

client = HJSClient(api_key="your-key")
result = client.judgment("user@example.com", "approve")
print(result['id'])  # jgd_1234567890abcd
```

### JavaScript
```javascript
import HJSClient from '@hjs/sdk-js';

const client = new HJSClient({ apiKey: 'your-key' });
const result = await client.judgment({
  entity: 'user@example.com',
  action: 'approve'
});
console.log(result.id);  // jgd_1234567890abcd
```

### CLI
```bash
hjs judgment create --entity user@example.com --action approve
```

### Rust
```rust
use hjs_core::JudgmentEvent;

let event = JudgmentEvent::new("user@example.com", "approve");
let receipt = event.sign()?;
assert!(receipt.verify()?);
```

## Why HJS?

- ✅ **Minimal** — Only four primitives, easy to implement
- ✅ **Portable** — Cryptographic receipts work across any system
- ✅ **Verifiable** — Third-party verification without trust
- ✅ **Standards-based** — IETF standardization in progress
- ✅ **Multi-language** — Rust, Python, JavaScript, CLI
- ✅ **Privacy-preserving** — No personal data collection

## Contact

- **Email**: [signal@humanjudgment.org](mailto:signal@humanjudgment.org)
- **GitHub Issues**: Use individual repository issues

## License

- **Protocol Specification**: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
- **Code Implementations**: [MIT](https://opensource.org/licenses/MIT) or [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) (see individual repositories)

---

**© 2026 HJS Foundation Ltd.**
