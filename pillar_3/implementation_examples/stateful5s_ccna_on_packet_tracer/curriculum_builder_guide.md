# 📖 Curriculum Builder Guide: Stateful5s Creator Kit

This guide provides the exact operational steps to build your curriculum. Follow these instructions in order; do not skip any step, as the stateful nature of this system depends on the manual integrity of this loop.

---

## 1. Initial Curriculum Setup
Before starting the Stateful5s loop, prepare your environment:
1. **Define the Themes:** Generate your initial curriculum themes following the standard Coding5s methodology, using the generator prompt included in `generate_lessons_ccna_on_packet_tracer_prompt_phase_1.md` and then with the prompt `generate_lessons_ccna_on_packet_tracer_prompt_phase_2.md`.
2. **Build the Skeleton:** Create the structural table for your lesson plan and paste it in the Stateful5s Creator Kit.

---

## 2. Operational Workflow (The Generation Loop)

### Stage 1: Topic Context Generation
1. **Locate the Formula:** Go to the **Prompt Topic Context** column. It contains a formula that pulls data from `#`, `Lesson Name`, and `Steps to Perform`.
2. **Generate:** Allow the formula to calculate the content for the `Topic Context` cell.
3. **Commit Data:** Copy the resulting text from the `Prompt Topic Context` cell and **Paste as Values** into the relative cell in the **Topic Context** column.
   * *Note for Lesson 1:* Manually input the values for `IA Name`, `Objective`, `New Concepts`, and `Steps to Perform`. For all lessons after the first, these will be filled automatically by the workflow below.

### Stage 2: Lesson State Generation (The Sanitization Loop)
1. **Identify the Prompt:** Go to the **Lesson Prompt** column. This cell contains the logic that references `Level`, `Type`, `Lesson Name`, `Topology`, and the `Accumulated Context` of the previous lesson.
2. **Execute:** Run this prompt in your LLM of choice.
3. **Paste for Sanitization:** The LLM will return a structured table. Copy this table and **Paste as Values** into cell **C79**.
4. **Finalize Row Data:** Copy the data range **C80:J80** from the sanitization area and **Paste as Values** into the corresponding row in the `#` column (from `#` through `Steps to Perform`).
5. **Verify:** At this point, the row is complete. The formula in the **Accumulated Context** column will automatically pick up the `Topic Context` and start building the chain for the next lesson.

### Stage 3: Professional Lesson Generation
1. **Final Prompt:** Go to the **Lesson Prompt Generator** column.
2. **Deploy:** Use this prompt in your LLM. It automatically pulls data from `#`, `Level`, `Type`, `Lesson Name`, `IA Name`, `Objective`, `New Concepts`, `Steps to Perform`, and the injected `Accumulated Context`.
3. **Result:** The LLM will now generate the final, professional Socratic lesson for the student, fully aware of all prior network configurations.

---

## 3. Iteration
Repeat the entire process described in **Stage 1 through Stage 3** for every subsequent lesson until your course is complete.

*   **Warning:** Because this is a stateful architecture, you cannot extend a formula across the entire column. You must execute this manual loop for every single row to ensure the `Accumulated Context` remains accurate.
*   **Completion:** Once all rows are processed, your **Stateful5s Creator and Student Kits** are ready for deployment.

## 4. Video With Instructions
A video with the instructions is in the making process.