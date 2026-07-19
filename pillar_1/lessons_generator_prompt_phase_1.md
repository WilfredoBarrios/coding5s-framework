# 📋 Prompt: Programming Language Curriculum Generation (Phase 1)

This prompt is designed for **Phase 1: Domain Blueprint Generation** within the standard Coding5s framework. It exhaustively maps the syntax, paradigms, and modules of a programming language into an analytical ledger before generating any lesson tables.

---

```text
[TECHNOLOGY/SKILL]: Elixir (o Python, Pandas, etc.)
[INCLUDE OOP]: NO 
[EXCLUSIONS]: (Ej: OTP Avanzado, GenServers, Supervisors)
[MANDATORY_BRIDGES]: (Ej: Recursión, TCO, Streams, I/O Archivos, Procesos Primitivos, Modelo Actor)
[ADDITIONAL TOPICS]: (Ej: Ecto básico)
[OUTPUT LANGUAGE]: Spanish

---
Act as a Senior Technical Curriculum Architect. This is PHASE 1 of a curriculum generation process. Your ONLY job is to analyze the technology exhaustively, map the subdomains, and calculate the EXACT number of topics required based on strict grouping logic. DO NOT generate the final curriculum table.

Please follow these STRICT rules:

1. **EXHAUSTIVE SCOPE & ANTI-OVER-PRUNING (CRITICAL):**
   * Focus ONLY on native features of [TECHNOLOGY/SKILL]. You MUST be exhaustive. Do not skip or hide core language features, operators, or common standard library modules just to save space.
   * STRICTLY BAN anything listed in [EXCLUSIONS].
   * **ANTI-OVER-PRUNING RULE:** When excluding advanced domains, do NOT prune their fundamental prerequisites. 
   * **MANDATORY BRIDGES:** You MUST integrate every concept listed in [MANDATORY_BRIDGES] as dedicated topics and subdomains. These act as the ultimate preparation layer.
   * Include [ADDITIONAL TOPICS] if provided.
   * If [INCLUDE OOP] is 'NO', strictly ban all Object-Oriented Programming concepts. If 'SÍ', include them.

2. **THE "TOOLBOX" GROUPING RULE (CRITICAL):**
   * Group functions, methods, or operators into a SINGLE topic ONLY IF they share the exact same mental model and syntactic footprint (e.g., "String Formatting", "Logical Operators", "Basic Arithmetic").
   * BANNED: Do NOT separate sibling methods into individual topics (e.g., Do NOT make one topic for `lower()` and another for `upper()`).
   * BANNED: Do NOT condense concepts from different syntactic families (e.g., Do NOT group project creation like `mix new` with function definition like `defmodule`).

3. **THE OVERSPILL RULE (MAX 5 VARIANTS PER TOPIC):**
   * A single topic can hold a MAXIMUM of 5 methods, functions, or variants.
   * If a conceptual family has more than 5 common tools (e.g., 10 common String methods or 12 Enum functions), you MUST split it into sequential topics (e.g., "String Methods Part 1 (lower, upper, strip, replace, split)", and "String Methods Part 2 (...)").
   * This forces balanced granularity. Do not cheat by omitting important methods just to avoid creating more topics.

4. **NO PROJECTS RULE (CRITICAL):**
   * DO NOT include any 'Project' or 'Capstone' topics in this ledger. Your output must consist STRICTLY of standard theoretical and mechanical topics. Projects will be dynamically injected by a separate engine in Phase 2.

5. **OUTPUT STRUCTURE:**
   Format your response EXACTLY with these three sections using clean markdown lists (NO markdown tables):

   ### 🗺️ 1. Domain Blueprint
   List the major conceptual subdomains that will be covered exhaustively (e.g., Primitive Types, Control Flow, Collections, etc.), ensuring [MANDATORY_BRIDGES] are included.

   ### 🧮 2. Topic Calculation Ledger
   Break down each subdomain from section 1 and list the theoretical topics inside it, showing the grouped methods in parentheses to prove they respect the Toolbox and Overspill rules (Max 5 per topic).
   *Example Format:*
   - **Subdomain: Strings**
     - Topic: String Creation & Interpolation
     - Topic: String Methods Part 1 (lower, upper, strip, replace, split)
     - Topic: String Methods Part 2 (capitalize, contains?, starts_with?)

   ### 📐 3. Final Metric Contract
   Provide the final calculated numbers based on the Ledger. You MUST output exactly this list:
   * Total Topics (Standard): [Number]
   * GRAND TOTAL ROWS: [Number]

Remember: DO NOT generate the curriculum table. Only provide the analytical blueprint.


```
