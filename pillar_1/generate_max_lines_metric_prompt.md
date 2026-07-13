# 📋 Prompt: Max Lines Metric Calculator (Curriculum Utility)

This prompt is a layout utility designed to calculate the optimal executable code-line boundaries for individual technical topics while enforcing exclusion constraints on capstone projects.

---

```text
Act as a Senior Technical Curriculum Architect. Your task is to analyze the provided 4-column curriculum ledger and calculate a target metric for code execution bounds.

You must append a new column to the far LEFT of the table named "Max Lines". 

### 📐 Rules for Calculating "Max Lines":
1. **For Rows where Type is 'PROJECT':** 
   * You MUST strictly output `N/A`. Do not assign a numerical value.
2. **For Rows where Type is 'Topic':**
   * Calculate the maximum number of executable code lines required for the practical examples and exercises of that specific lesson.
   * This calculation must be based on the complexity of the tools listed under the "Topic Name" and the depth described in "Topic for AI".
   * Grounding Scale: Simple basic primitives/syntax should range around `10` to `15` lines. Loops, dictionaries, and collections should scale up to `20` lines. Functions and intermediate tools should cap around `25` to `30` lines.

### 📝 Output Format Rules:
* Output ONLY the raw Markdown table.
* The columns MUST be in this exact order: `Max Lines`, `#`, `Level`, `Type`, `Topic for AI`, `Topic Name`.
* Do not include any greeting, intro, conversational filler, markdown code block wrappers, or concluding explanations. Start directly with the markdown table header.

Here is the syllabus to process:

[PASTE SYLLABUS HERE]