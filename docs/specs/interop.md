# Interoperability Specification

## Objective

Enable UXI-LLM to be embedded, invoked, or extended from any major language or platform with minimal friction. The system prioritizes shared memory bridges, RPC, and native bindings across ecosystems.

---

## Supported Languages (Initial Target)

- 🐍 Python
- 🌐 JavaScript / TypeScript
- ⚙️ Rust
- ☕ Java / Kotlin
- 🧱 C / C++
- 💻 WASM (WebAssembly environments)

---

## Integration Methods

| Method       | Description                               | Status   |
|--------------|-------------------------------------------|----------|
| FFI (C ABI)  | Shared object + header export             | ✅ Stable |
| RPC          | JSON-RPC and WebSocket endpoint support   | 🔄 Beta   |
| WASM         | Embedded WASM runtime (experimental)      | 🔬 Proto  |
| HTTP API     | REST/GraphQL interface to runtime         | ✅ Stable |

---

## Embedding Example (Python)

```python
from uxi import load_model

model = load_model("uxi-transformer-v1")
response = model.run("What is the capital of France?")
print(response)
