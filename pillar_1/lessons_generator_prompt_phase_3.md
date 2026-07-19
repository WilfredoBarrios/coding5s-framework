# 📋 Prompt: Curriculum Table Generation (Phase 2)

This prompt is designed for **Phase 2: Curriculum Table Generation** within the Coding5s framework. Use it to cleanly sanitize and transform your raw list of programming language topics into a flat structured table.

---

```text
Act as a Senior Technical Curriculum Designer. This is PHASE 2 of the curriculum generation process for the Coding5s Framework. I will provide you with the audited "Topic Calculation Ledger" from Phase 1. 

Your ONLY job is to transform that ledger into a highly detailed, tabular Master Curriculum for Micro-Learning, strictly ensuring specific column constraints and injecting projects.

Please follow these STRICT rules:

1. STRICT ORDER PRESERVATION (CRITICAL):
   * You MUST preserve the EXACT sequential order of the topics as they appear in the Phase 1 Input Ledger. 
   * BANNED: You are strictly forbidden from sorting, grouping, moving, or reordering any topics. Read the ledger top-to-bottom and output the rows in that exact same sequence.
   * ANTI-SUMMARIZATION & CLEANUP RULE: Do NOT truncate, simplify, or abstract the core topic names. You MUST preserve the exact concepts, operators, and methods listed in the parentheses from the Phase 1 Ledger. HOWEVER, you MUST strip the literal prefix "Topic: " from the string before placing it in the table.

2. DYNAMIC PROJECT INJECTION (NO DELETION RULE):
   * As you iterate down the original list, you MUST automatically inject one row of Type 'PROJECT' approximately every 7 to 8 'Topic' rows.
   * CRITICAL: Inserting a project means ADDING A BRAND NEW ROW. You are strictly forbidden from overwriting, deleting, or replacing any existing topic from the Ledger. The total row count will EXPAND.
   * SCOPING RULE: A Project must ONLY consolidate the concepts from the preceding 7 to 8 topics.
   * Give each project a descriptive `Topic Name` and an actionable `Topic for AI`.

3. IN-PLACE LEVEL ASSIGNMENT:
   * Evaluate the technology in each topic and assign its 'Level' column in-place:
     - Beginner: Core syntax, basic types, primitive operators, basic control flow, and simple collections.
     - Intermediate: Functions, classes/objects, advanced collection manipulation, standard error handling, and basic architecture.
     - Advanced: Concurrency, async programming, streams, memory management, complex design patterns, file I/O.

4. THE "TOPIC FOR AI" INSTRUCTION (CRITICAL):
   * This column MUST be a strict, imperative instruction for an AI tutor.
   * It MUST start with an action verb (e.g., "Evaluate", "Create", "Assign").
   * EXPLICIT MENTION RULE: For 'Topic' rows, you MUST explicitly write out EVERY SINGLE method, operator, or function variant listed in the Ledger's parentheses. DO NOT generalize.
   * PROJECT EXCEPTION: For 'PROJECT' rows, DO NOT list every single tool. Instead, write a concise, natural sentence focusing on the consolidation goal (e.g., "Develop a CLI tool consolidating Core Types, Operators, and Null Safety.").

5. MAX LINES ESTIMATION (`Max Lines`) & COMPLEXITY CALCULATION:
   * You MUST assign a strict integer representing the maximum number of executable code lines needed to practice the syntax. Do not use text or ranges.
   * DYNAMIC CALCULATION FOR MICRO-LEARNING: Keep the code short and focused:
     - Low Complexity (Variables, primitive operators, basic types): 8 to 12 lines.
     - Medium Complexity (Control flow, loops, functions, basic collections): 12 to 18 lines.
     - High Complexity (Classes, async/await, concurrency, error handling): 18 to 25 lines.
   * PROJECT CONSTRAINTS: For 'PROJECT' rows, the number must be larger to allow consolidation, but strictly bounded. Keep projects between 25 and 35 lines maximum.

6. EXAMPLES QUANTITY CALCULATION (`Examples Qty`):
   * 3: Basic, single-action syntax.
   * 4: Intermediate logic, branching.
   * 5: Multi-step transformations, pipelines, concurrency.
   * 0: For ANY row where `Type` is 'PROJECT'.

7. SYNTHETIC DATA EVALUATION (`Synthetic Data`):
   * Output "No" (DEFAULT): For almost all topics.
   * Output "Yes": ONLY when absolutely indispensable (e.g., File I/O, DB operations, HTTP parsing).

8. MARKDOWN TABLE CORRUPTION PREVENTION (CRITICAL):
   * You are strictly FORBIDDEN from using the raw pipe character (`|`), or any slash-escapes like `\|` or `\vert{}` inside cell text, as they break Markdown/CSV parsers.
   * If the syntax involves a pipe (like OR operators), simply replace it with the word 'OR' or a comma `,`.

9. TABLE STRUCTURE (STRICT ORDER):
   Create a markdown table with exactly these 8 columns in this EXACT order:
   1. Max Lines
   2. Examples Qty
   3. Synthetic Data
   4. # (Sequential Row Number, from 1 to the end, including injected Projects)
   5. Level (Beginner, Intermediate, Advanced)
   6. Type (Topic or PROJECT)
   7. Topic for AI (Must contain the specific methods)
   8. Topic Name (Must strip the "Topic: " prefix, but include the parentheses and all items)

10. BATCH GENERATION (ANTI-TIMEOUT):
   * Output ONLY rows 1 to 30.
   * HEADER: `### Master Curriculum: Part 1 (Rows 1-30)`
   * FOOTER: `⚠️ **SECURITY PAUSE:** I have generated the first 30 rows. Type **'Continue'** to generate the next block.`

---
INPUT LEDGER FROM PHASE 1:
[PASTE YOUR AUDITED PHASE 1 LEDGER HERE]


```