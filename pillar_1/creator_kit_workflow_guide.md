# 🛠️ Step-by-Step Guide: Creating a New Course with the Coding5s Creator Kit

This guide outlines the precise execution sequence required to initialize, populate, and audit a new programming language curriculum within the data ledger framework. Follow these steps sequentially to prevent reference breakage and context corruption.

---

### ⚠️ Critical Architecture Note
This onboarding process is highly advanced and demands a solid grasp of complex Excel reference mechanics. However, it is a highly specific, predictable task: your main engineering objective during the formula transfer is simply ensuring that the structural matrix layout respects every cell mapping precisely without generating reference errors (`#REF!`, `#VALUE!`). 

*(Note: An in-depth instructional video walk-through demonstrating this exact formula-injection process is currently in the makings).*

---

### Step 1: Syllabus Generation & Data Ingestion
1. Open the repository and locate `lessons_generator_prompt_phase_1.md` and `lessons_generator_prompt_phase_2.md`.
2. Run the Phase 1 prompt in your LLM to generate the exhaustive domain blueprint for your target technology.
3. Pass the resulting blueprint into the Phase 2 prompt to compile a sanitized 4-column flat Markdown table.
4. Copy the structured table output and paste it directly into the **`PromptGenerator`** sheet starting at row 9, filling out the `#`, `Level`, `Type`, and `Topic Name` fields.

### Step 2: Extracting and Customizing Paradigm & Ecosystem Rules
1. Navigate to the rule engine tabs (**`FGen_S1`** to **`FGen_S2`**).
2. Execute the embedded rule-generation prompts in your LLM to obtain the baseline constraints for the **`Paradigm & Ecosystem`** category. 
   > **Note:** These are the *only* rules you should modify. All other structural rules act as the immutable baseline that guarantees output shape consistency.
3. Copy the generated rule tags and their corresponding descriptions.
4. Highlight the range containing the entries under the **"Rule Tag"** column and the values under **"Rule To Concatenate"** column.
5. Paste these entries as active variables directly beneath the main prompt interface to anchor them as a systematic reference matrix.
6. The system will auto-populate a layout grid containing the specialized constraints for the target programming language.

### Step 3: Manual Rule Auditing and Architecture Cross-Referencing
1. Review the newly generated language rules row-by-row to ensure structural and technical accuracy.
2. Modify rows manually where adjustments are required.
3. When constructing rules within the **"Rule To Concatenate"** column:
   * You can input standard string configurations directly.
   * If a rule requires dynamic context embedding or dynamic references, open the baseline **Python** configuration layout to cross-examine how its formulas and dependencies were structurally assembled.

### Step 4: Compiling, Sanitizing, and Injecting Master Formulas
1. Locate the highlighted green tracking block in the spreadsheet.
2. Select the entire vertical range of green cells, stretching precisely from the top dark-green boundary cell down to the bottom dark-green tracking limit.
3. Copy the highlighted range and paste it directly into an empty text document using **Notepad** (or a plain text editor).
4. **Character Limit Check:** Verify the total string character footprint inside your text editor. The payload must strictly remain below **8,190 characters** to satisfy the native constraint limits of Microsoft Excel.
5. Highlight and select the entire sanitized formula string directly inside Notepad, then copy it.
6. Return to your active spreadsheet grid and paste the formula payload directly into the first active lesson cell of the target Stage column:
   * **For Standard Topics (Stage 1):** Paste into cell **`K9`** (`Stage 1 Prompt`).
   * **For Project Tracks (Stage 1):** Paste into cell **`Z9`** (`Stage 1 Project`).
   * **For AI Technical Mentors:** Paste into cell **`L9`** (`Mentor Prompt`).
7. Drag or fill the newly modified formula cell vertically down through all subsequent rows in the matrix.
8. **Reference Validation:** Thoroughly audit the filled matrix columns to guarantee that relative row mappings remain unified and that no absolute cell anchors were broken or shifted during expansion.

### Step 5: Sandbox Testing and Output Verification
1. Select random generated prompts out of the completed `Lesson Prompt Generator` array rows.
2. Feed these compiled payloads into your target LLM environment to review the rendering behavior.
3. Audit the generated practical exercises to verify they accurately honor the target parameters (such as the mandatory executable line boundaries specified in `Max Lines`).
4. If the structural layout or technical content breaks constraints, revisit the sheet cell definitions, adjust the variables, and debug your concatenation layout until the prompt output stabilizes.