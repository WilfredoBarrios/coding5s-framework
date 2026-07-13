# 📋 Prompt: Curriculum Table Generation (Phase 2)

This prompt is designed for the **Phase 2: Curriculum Table Generation**. Use this to transform your raw list of topics into the structured Markdown table required for the Stateful5s Creator Kit.

---

```text
Act as a Senior Network Lab Architect and CCNA Instructor specialized in creating highly operational, stateful, and strictly practical curricula for Cisco Packet Tracer.

I will provide you with a raw list of CCNA lessons. Your task is to transform this list into a clean Markdown table with the following **exact columns** in this order:

1. #
2. Level
3. Type
4. Lesson Name

**STRICT RULES FOR GENERATION:**

1. **Preserve Original Content and Order:**
   Keep the exact lesson numbers, levels, types, original lesson names, and lesson order provided in the source list.

2. **Do Not Generate Additional Information:**
   Do not create objectives, AI names, concepts, steps, descriptions, explanations, or any other content not included in the four required columns.

3. **Output Format:**

   * Output **ONLY** the Markdown table.
   * Use exactly these column headers: `#`, `Level`, `Type`, and `Lesson Name`.
   * Do not include any additional columns.
   * Do not add any text, greetings, notes, explanations, or conclusions before or after the table.

Now process the following syllabus and generate the complete table:

[PASTE LESSONS HERE]