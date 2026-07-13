# ⚙️ Core Specifications: Stateful5s Data Ledger

> **Technical definition of the 13-column Architectural Ledger schema.**

This document provides the canonical definition for every column in the Stateful5s Creator Kit. It serves as the primary reference for the data contract required to maintain state persistence across curriculum transitions.

---

## 1. Column Definitions

| Column Name | Source | Purpose |
| :--- | :--- | :--- |
| **#** | Manual / Auto | Unique lesson identifier and row index. |
| **Level** | Manual | Defines instructional depth (Beginner, Intermediate, Advanced). |
| **Type** | Manual | Classification of the transition (STEP, CHECKPOINT, etc.). |
| **Lesson Name** | Manual | Formal title of the current technical module. |
| **IA Name** | Manual | Friendly persona identifier for the AI instructor. |
| **Objective** | LLM / Manual | Defines the pedagogical goal for the student. |
| **New Concepts** | LLM / Manual | Lists specific technical concepts introduced in the lesson. |
| **Steps to Perform** | LLM / Manual | Granular list of instructions for the student/Packet Tracer setup. |
| **Topic Context** | LLM / Formula | Contains the context generated from the specific lesson steps. |
| **Topology Expansion** | Manual | Records events adding hardware or network segments. |
| **Prompt Topic Context** | Formula | Automates the creation of the current lesson's `Topic Context`. |
| **Lesson Prompt** | Formula | Generates the prompt to trigger the FSM transition logic. |
| **Accumulated Context** | Persistent | **The State Engine:** Serialized state of the entire network configuration. |
| **Lesson Prompt Generator** | Formula | Final instruction payload to generate the student-facing lesson. |

---

## 2. Column Logic & Dependencies

* **Manual Columns:** `Level`, `Type`, `Lesson Name`, `IA Name`, `Topology Expansion`. These define the "initial state" for any given row.
* **Formula-Driven Columns:** `Prompt Topic Context`, `Lesson Prompt`, `Lesson Prompt Generator`. These are the FSM engines that transform inputs into actionable instructions.
* **Derived Columns:** `Objective`, `New Concepts`, `Steps to Perform`, `Topic Context`. These contain the generated content that flows through the generation loop.
* **Persistent Column (`Accumulated Context`):** The most critical column. It concatenates the state of previous lessons to maintain topological determinism and prevent AI hallucinations.

---

## 3. Data Integrity & State Propagation

To ensure the state machine remains functional, the following rules apply:

1.  **Formulas vs. Values:** The formula-driven columns generate the structure, but the content must be committed as **Static Values** (Paste Special → Values) to ensure the historical state is frozen.
2.  **State Chain:** The `Accumulated Context` acts as the primary feedback loop. Any row without a correctly populated `Accumulated Context` cell will break the continuity of the curriculum.
3.  **Expansion Logic:** `Topology Expansion` must be manually updated by the architect whenever new infrastructure (routers, switches, links) is added, ensuring the LLM is aware of the expanded physical surface.

---

## 4. Operational Role of the Ledger
The ledger serves as a persistent "Architectural Ledger." It is not merely a table, but a **state machine**. Each row is a transaction that updates the current configuration of the network. Because state is cumulative, the system cannot be calculated via a single global spreadsheet formula; each row must be validated and committed before the next state can be generated.