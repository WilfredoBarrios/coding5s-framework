# 🛠️ Formula Auto-Injector (Prompt Formulas Paster)

The **Formula Auto-Injector** is an advanced automation script for the **Coding5s** educational framework. It automates the extraction, validation, and multi-range batch injection of complex prompt-generation formulas from the modular generation sheets (`FGen_S1` through `FGen_S5`) directly into the master `PromptGenerator` sheet of a specified **Creator Kit**.

---

## 💡 Why This Tool Matters

When building or updating curriculum modules in the *Coding5s* ecosystem, prompt logic is structured into atomic blocks across five stages (`FGen_S1` to `FGen_S5`). Traditionally, this required a tedious manual workflow: selecting green generator ranges, copying them, pasting them into Notepad to clean formatting, opening the `PromptGenerator` sheet, initiating cell editing, pasting the formula, and dragging/extending it down to row 200 for Topics, Projects, and Mentors across all five stages.

This automated injector solves that friction completely:

* **Eliminates Clipboard Conflicts:** Bypasses Windows clipboard and cell-editing limitations by reading cell values and injecting `.Formula` strings directly through memory (COM Automation).
* **Native Excel Dynamic Scaling:** Instead of simulating manual mouse dragging, it targets entire ranges (e.g., `K9:K200`) at once. Excel's native engine automatically adjusts relative row references cleanly across all 200 rows.
* **Built-in Safety Guard (8,100 Character Limit):** Microsoft Excel enforces a strict limit of 8,192 characters per formula cell. Before writing anything, the script measures the compiled formula length. If any stage exceeds 8,100 characters, the script **halts instantly, aborts changes (`wb.Close(False)`), and alerts the creator**, fully protecting the workbook from corruption.


* **Targeted Single-File Precision:** Operates on a single, user-defined *Creator Kit* in the local directory, giving complete control during active course development.



---

## ⚙️ Target File Configuration

To specify which *Creator Kit* to update, adjust the configuration block at the top of `copy_paster_Prompt_Formulas_for_CK.py` (or your custom script filename):

```python
# ==========================================
# ⚙️ MAIN CONFIGURATION
# ==========================================
# 1. Exact filename of the Creator Kit you are editing in the root folder
ARCHIVO_CREATOR_KIT = "Coding5s Python Core & Scripting v0.4 Creator Kit.xlsx" 

# 2. Safety limit
LIMITE_CARACTERES = 8100
PESTANA_DESTINO = "PromptGenerator"
FILA_FIN = 200
# ==========================================
```[cite: 9]

---

## 📂 System Architecture & Components

To run the auto-injector pipeline, the working directory must contain the Python engine, the batch runner, and your target *Creator Kit*:

```text
pillar_1/coding5s_creator_kits/
│
├── 🐍 copy_paster_Prompt_Formulas_for_CK.py  <-- Core Python auto-injector engine[cite: 10]
├── ⚙️ Creator Kit Updater Runner.bat         <-- 1-Click execution script[cite: 10]
├── 📖 formula_injector_guide.md              <-- Documentation
│
└── 📊 Coding5s Python Core... Creator Kit.xlsx <-- Target Creator Kit[cite: 9]

```

### 1. `copy_paster_Prompt_Formulas_for_CK.py`

The **Core Python Automation Engine**. Handles independent COM instantiation (`DispatchEx`), reading source coordinate arrays (`FGen_S1` to `FGen_S5`), validating character lengths, and batch-injecting formulas into `PromptGenerator`.

### 2. `Creator Kit Updater Runner.bat`

The **1-Click Execution Script**. Triggers a native VBScript confirmation dialog detailing the scope of the macro before launching the Python script.

---

## 🔄 How the Auto-Injection Process Works

When triggered, the engine executes a strict 4-step execution pipeline:

1. **File Existence Validation:**
Verifies that the target file specified in `ARCHIVO_CREATOR_KIT` exists in the local directory. If not found, it prints a critical error and exits safely.


2. **Isolated Background Engine Initialization (`DispatchEx`):**
Launches a completely independent, invisible instance of Excel in memory (`Visible = False`, `ScreenUpdating = False`, `Interactive = False`), preventing interface flickering or window stealing.


3. **Coordinate Mapping & Formula Assembly:**
Iterates through the pre-configured coordinate map (`MAPA_FORMULAS`) covering all 5 stages (Topics, Projects, and Mentors):


* Reads source cell ranges (e.g., `E3:E50` in `FGen_S1`).


* Extracts text values row by row, discarding empty cells (`None`), and joins them using newline characters (`\n`)—replicating the exact function of manual Notepad text cleaning.




4. **Safety Verification & Range Injection:**
* **Length Check:** If `len(formula_texto) > 8100`, it immediately halts execution, closes the workbook without saving (`wb.Close(False)`), and outputs a red error log specifying the offending stage and range.


* **Batch Assignment:** Injects the compiled formula text into the full destination column range (e.g., `K9:K200`) in one atomic operation, causing Excel to auto-expand references natively.




5. **Native Save & Memory Cleanup:**
If all stages pass without errors, it saves the workbook (`wb.Close(True)`), restores screen updating/events, and quits the background Excel process cleanly.



---

## 🚀 Setup & Requirements

### System Requirements

* **Operating System:** Windows 10/11
* **Software:** Microsoft Excel installed locally
* **Environment:** Python 3.8+

### Dependencies

Ensure the Windows COM extension package is installed via terminal:

```bash
pip install pywin32

```

---

## 💻 Step-by-Step Execution

1. **Configure Target Filename:**
Open your script file, update `ARCHIVO_CREATOR_KIT` with the exact filename of the *Creator Kit* you are currently editing, and save.


2. **Verify File Placement:**
Ensure the script, batch runner, and target *Creator Kit* reside together in the same directory.


3. **Execute the Injector:**
Double-click **`Creator Kit Updater Runner.bat`**. Click **OK** on the native confirmation prompt.


4. **Monitor Console Output:**
The command prompt will display real-time injection metrics and character counts for every stage:
```text
==================================================
🚀 INICIANDO AUTO-INJECTOR DE FÓRMULAS CODING5S
==================================================

Archivo objetivo: Coding5s Python Core & Scripting v0.4 Creator Kit.xlsx
Abriendo archivo en memoria...

Procesando FGen_S1 (E3:E50)  =>  PromptGenerator!K9:K200 ...
  ✅ Inyección exitosa. Largo de la fórmula: 7042 caracteres.
Procesando FGen_S1 (E54:E79)  =>  PromptGenerator!Z9:Z200 ...
  ✅ Inyección exitosa. Largo de la fórmula: 4120 caracteres.
...
💾 Guardando archivo...
🎉 ¡TODAS LAS FÓRMULAS FUERON ACTUALIZADAS CON ÉXITO!
Proceso finalizado. Memoria limpia.

```


5. **Completion:**
Press any key to exit the terminal. Open your *Creator Kit* to verify that all prompts across all stages have been instantly generated and rendered.