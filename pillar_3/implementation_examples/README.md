# 🚀 Stateful5s: Implementation Examples

This directory houses the practical implementations of the **Stateful5s Architecture**. Each sub-folder contains a specific curriculum built using the state-machine logic to ensure context persistence across complex infrastructure laboratories.

## 📂 Active Implementations

*   **[stateful5s_ccna_on_packet_tracer](./stateful5s_ccna_on_packet_tracer/)**: The flagship implementation. A full CCNA lab series (103 lessons) for Packet Tracer, managed via a persistent state ledger.

## 🎯 Implementation Goals
Each implementation in this directory follows the core Stateful5s principles:
1.  **State Persistence:** Every lab configuration is tracked via a Ledger.
2.  **Context Injection:** No hallucinations; every lesson knows the exact state of the network from previous steps.
3.  **Zero-Cloud Cómputo:** Built for local simulation environments, optimized for resource efficiency.

## ➕ Adding a New Course
To implement a new course using Stateful5s:
1.  Create a new directory (e.g., `stateful5s_cloud_aws_labs`).
2.  Include your specific `Creator Kit` (Ledger matrix).
3.  Document the workflow and dependencies in a local `README.md` following the Stateful5s standard.

---
*For more information on the architecture, refer to the [Pillar 3 Main Repository](../README.md).*