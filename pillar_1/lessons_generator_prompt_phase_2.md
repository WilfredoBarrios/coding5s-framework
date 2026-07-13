# 📋 Prompt: Curriculum Table Generation (Phase 2)

This prompt is designed for **Phase 2: Curriculum Table Generation** within the Coding5s framework. Use it to cleanly sanitize and transform your raw list of programming language topics into a flat structured table.

---

```text
Act as a Senior Technical Curriculum Designer. This is PHASE 2 of the curriculum generation process. I will provide you with the "Topic Calculation Ledger" from Phase 1. 

Your ONLY job is to transform that ledger into a highly detailed, tabular Master Curriculum for Micro-Learning, strictly ensuring level progression consistency.

Please follow these STRICT rules:

1. **STRICT LEVEL CLUSTERING & REORDERING (CRITICAL):**
   * Before generating the table, you MUST group and sort all topics from the Phase 1 Ledger by their conceptual difficulty level. 
   * **The Order MUST be:** Group ALL 'Beginner' topics first, followed by ALL 'Intermediate' topics, and finally ALL 'Advanced' topics.
   * **BANNED:** You are strictly forbidden from placing an Intermediate or Advanced topic before or between Beginner topics (e.g., Do NOT place "Binaries & Bitstrings" until all basic text, lists, tuples, and basic match operators are completed).
   * **ANTI-SUMMARIZATION RULE:** Do NOT truncate, simplify, or abstract the topic names during reordering. You MUST preserve the exact concepts, operators, and methods listed in the parentheses from the Phase 1 Ledger.

2. **DYNAMIC PROJECT INJECTION BY LEVEL:**
   * After sorting the theoretical topics by level, you MUST automatically inject one row of Type 'PROJECT' approximately every 7 to 8 'Topic' rows.
   * **SCOPING RULE:** A Project injected inside the Beginner cluster can ONLY use and consolidate Beginner concepts. A Project injected inside the Intermediate cluster will consolidate Intermediate and Beginner concepts, and so on.
   * Give each project a descriptive `Topic Name` and an actionable `Topic for AI`.

3. **LEVEL DEFINITION CONTRACT:**
   * Ensure topics are classified under these strict parameters:
     - **Beginner:** CLI tools, Numeric types, Atoms/Booleans, basic Arithmetic, Logical and Comparison operators, String manipulation/modifiers/splitting, basic Tuples, basic Linked Lists, and basic List/Map APIs, plus the core Match (=) and Pin (^) operators.
     - **Intermediate:** Advanced map manipulation, Keyword lists, Module definition (`defmodule`), Named functions (`def/defp`), multi-clauses, Functional Guards (`when`), Anonymous functions (`fn`), Capture operator (`&`), Pipe operator (`|>`), basic control flow (`if`, `case`, `cond`), and Recursion/TCO.
     - **Advanced:** Binaries & Bitstrings (`<<>>`), Streams (lazy evaluation), Comprehensions (`for`), Structs (`defstruct`), Behaviours, Protocols, Error handling (`try/rescue/catch`), Files/Path I/O, Primitive Processes (`spawn`, `send`, `receive`), Process links/monitors/registration, and Ecto (Database infrastructure, schemas, changesets, queries).

4. **THE "TOPIC FOR AI" INSTRUCTION (CRITICAL):**
   * This column MUST be a strict, imperative instruction for an AI tutor.
   * It MUST start with an action verb (e.g., "Evaluate", "Create", "Assign", "Extract", "Implement").
   * **EXPLICIT MENTION RULE:** You MUST explicitly write out EVERY SINGLE method, operator, or function variant listed in the Ledger's parentheses for that specific topic. DO NOT generalize.

5. **EXAMPLES QUANTITY CALCULATION (`Cant. Ejemplos`):**
   * **3:** Basic, single-action syntax (e.g., arithmetic, basic variables, pin operator).
   * **4:** Intermediate logic (e.g., conditionals, pattern matching, recursion steps).
   * **5:** Multi-step transformations, pipelines (e.g., Enum chaining, Ecto queries, Streams).
   * **0:** For ANY row where `Type` is 'PROJECT'.

6. **SYNTHETIC DATA EVALUATION (`Synthetic Data`):**
   * **Output "No" (DEFAULT):** For almost all topics.
   * **Output "Yes":** ONLY when absolutely indispensable (e.g., File I/O, Ecto DB operations, or heavy Stream processing projects).

7. **MARKDOWN PIPE ESCAPE RULE (CRITICAL):**
   * Because you are generating a Markdown table, you MUST escape the pipe character if it appears inside a topic name or instruction. Use `\|` or `&#124;` so it does not break the table columns (e.g., for `\|>`, `\|\|`, or `[h \| t]`).

8. **TABLE STRUCTURE (STRICT ORDER):**
   Create a markdown table with exactly these 7 columns in this EXACT order:
   1. **Cant. Ejemplos** 2. **Synthetic Data** 3. **#** (Sequential Row Number, from 1 to the end, including injected Projects)
   4. **Level** 5. **Type** (Topic or PROJECT)
   6. **Topic for AI** (Must contain the specific methods from the parentheses)
   7. **Topic Name** (Must include the parentheses and all items inside them)

9. **BATCH GENERATION (ANTI-TIMEOUT):**
   * Output ONLY rows 1 to 30.
   * **HEADER:** `### Temario Maestro: Parte 1 (Temas 1-30)`
   * **FOOTER:** `⚠️ **PAUSA DE SEGURIDAD:** He generado los primeros 30 temas. Escribe **'Continúa'** para generar el siguiente bloque (31-60).`

---
**INPUT LEDGER FROM PHASE 1:**
[PASTE HERE ALL THE LESSONS GENERATED IN PHASE 1]

```