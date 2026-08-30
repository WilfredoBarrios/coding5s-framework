
# 🛠️ Sync Student Kit Generator

The **Sync Student Kit Generator** is an automated compilation and synchronization engine for the **Coding5s** educational framework. It scans the ecosystem's directory structure, reads master source files (**Creator Kits**), and compiles clean, production-ready distribution workbooks (**Student Kits**) without altering master files, formulas, or formatting layout.

---

## 💡 Why This Generator Matters

The core vision of **Coding5s** is to empower learners everywhere by making high-quality, prompt-driven programming education accessible worldwide, in any language.

Manually building and updating individual *Student Kits* across dozens of modules and multiple languages is time-consuming and error-prone. This generator solves that problem completely:

* **Global Accessibility & Fast Localization:** Anyone in the world who wants to distribute the **Coding5s** curriculum in their native language (e.g., Spanish, Swahili, French, Japanese, German) only needs to set their target language in the automation script. Running this tool automatically configures the master *Creator Kits* in memory and compiles a complete, fully localized suite of *Student Kits* ready for deployment.
* **Non-Destructive Creator Kit Protection:** The script opens *Creator Kits*, updates the language cell (`B6`), recalculates prompts in RAM, extracts static values, and closes the master file **without saving changes (`wb.Close(False)`)**. Master *Creator Kits* remain 100% untouched and pristine.
* **Single Source of Truth:** Creators only maintain content in one place (*Creator Kits*). The generator handles template cloning, in-memory language updates, cell mapping, and static value freezing automatically.
* **Scalability & Background Execution:** What used to take hours of manual copy-pasting, formatting, and filter removal now takes seconds. Using Windows COM Automation in "ghost mode" (`DispatchEx`), processing runs completely in the background without UI flickering or open Excel window interference.

---

## 🌍 Global Localization Workflow

To localize and publish a full course suite in any language:

1. Open `student_kit_creator.py` in your text editor or IDE.
2. Set the `RESULTS_IN_LANGUAGE` variable to your desired target language (e.g., `"English"`, `"Spanish"`, `"German"`, `"French"`).
3. Save the changes to `student_kit_creator.py`.
4. Run **`Student Kit Creator Runner.bat`**.

The generator will automatically process all *Creator Kits* in background memory, force Excel to recalculate all prompts, copy the master template (`Student Kit Template.xlsx`), transfer all generated micro-prompts and metadata into static values, clean up layout artifacts, and output ready-to-distribute **Student Kits** configured for that language.

---

## 📂 System Architecture & Components

To run the automated build process, the folder `coding5s_creator_kits` (under Pillar 1) must contain the core automation components alongside topic subdirectories:

```text
pillar_1/coding5s_creator_kits/
│
├── 📜 Student Kit Template.xlsx      <-- Master visual template
├── 🐍 student_kit_creator.py         <-- Core automation engine
├── ⚙️ Student Kit Creator Runner.bat  <-- 1-Click execution script
├── 📖 student_kit_creator_guide.md   <-- Documentation
│
├── 📁 python/                        <-- Language/topic subdirectories
│   ├── Coding5s Python Core... Creator Kit.xlsx
│   └── Coding5s Python Core... Student Kit.xlsx (Automatically generated)
├── 📁 elixir/
├── 📁 gleam/
└── 📁 dart/

```

### 1. `Student Kit Template.xlsx`

The **Master Visual Template**. It contains the clean student layout (`Coding5sStudentKit` sheet), pre-styled tables, brand colors, and structural protection settings.

* **Location:** Must reside in the same folder as `student_kit_creator.py`.
* **Role:** Serves as the blueprint. The script never alters this file; instead, it creates a clean clone of it inside each subfolder before injecting localized data.

### 2. `student_kit_creator.py`

The **Core Python Automation Engine**. It orchestrates file discovery, language simulation, RAM data extraction, template replication, and desktop-level Excel automation.

* **Key Configuration Variables:**
* `RESULTS_IN_LANGUAGE`: Set this variable at the top of the file to your target language (e.g., `RESULTS_IN_LANGUAGE = "English"`).
* `GRACIAS`: Protection password used to lock and unlock the Student Kit sheets.


* **Modules Used:**
* `os` & `shutil`: Recursive file system navigation and master template cloning.
* `win32com.client`: Background Windows COM Automation (`DispatchEx`) controlling Microsoft Excel. This forces formula recalculation upon language updates, performs RAM value extraction, and ensures zero corruption of XML table definitions, shapes, or conditional formatting extensions.



### 3. `Student Kit Creator Runner.bat`

The **1-Click Execution Script**. Displays a native VBScript confirmation dialog before launching the Python engine, allowing anyone on Windows to run the compilation pipeline with a simple double-click.

---

## 🔄 How the Build Process Works

When triggered, the engine executes the following pipeline:

1. **Global Template Validation:**
Verifies the presence of `Student Kit Template.xlsx` in the root folder. Aborts safely if missing.
2. **Recursive Folder Scanning (`os.walk`):**
Scans the directory and **all subdirectories** (`python`, `elixir`, `gleam`, `dart`, etc.) searching for Excel workbooks containing `"Creator Kit"` in their filename (ignoring active temporary files starting with `~$`).
3. **Isolated COM Initialization (`DispatchEx`):**
Launches a background, isolated instance of Excel (`Visible = False`, `ScreenUpdating = False`, `Interactive = False`).
4. **In-Memory Language Simulation & RAM Extraction:**
Opens each *Creator Kit*, sets cell **B6** on `PromptGenerator` to `RESULTS_IN_LANGUAGE`, and triggers `excel.Calculate()`.
* Extracts recalculated matrix **E9:Y200** directly from RAM into a Python variable.
* Extracts metadata range **I2:I3** directly from RAM.
* Closes the *Creator Kit* **WITHOUT SAVING (`wb.Close(False)`)**, leaving disk files completely untouched.


5. **Template Cloning (Student Kit Creation):**
For each *Creator Kit* found:
* Calculates target filename by replacing `"Creator Kit"` with `"Student Kit"`.
* Clones `Student Kit Template.xlsx` into the subfolder if the *Student Kit* does not exist.


6. **Desktop Ingestion (`win32com`):**
Opens the *Student Kit*, unprotects the sheet, and:
* Injects the static prompt matrix starting at cell **B9**.
* Injects module metadata into range **G2:G3**.
* Disables text wrapping (`WrapText = False`) across modified ranges to prevent layout distortion.
* Clears auto-filters (`AutoFilterMode = False`) for a clean initial view.


7. **Native Save & Structural Lock:**
Re-applies worksheet protection with the security password, saves changes (`wb.Close(True)`), and releases memory objects cleanly.

---

## 🚀 Setup & Requirements

### System Requirements

* **Operating System:** Windows 10/11
* **Software:** Microsoft Excel installed locally
* **Environment:** Python 3.8+

### Dependencies

Install the required Python package via terminal:

```bash
pip install pywin32

```

---

## 💻 Step-by-Step Execution

1. **Set Target Language:**
Open `student_kit_creator.py`, set `RESULTS_IN_LANGUAGE = "English"` (or target language), and save.
2. **Verify File Placement:**
Ensure `Student Kit Creator Runner.bat`, `student_kit_creator.py`, `Student Kit Template.xlsx`, and `student_kit_creator_guide.md` are inside `pillar_1/coding5s_creator_kits/`.
3. **Execute the Build:**
Double-click **`Student Kit Creator Runner.bat`**. Confirm the prompt dialog.
4. **Monitor Output:**
The terminal displays real-time status updates:
```text
Iniciando escaneo recursivo en: C:\github_repositories\coding5s-framework\pillar_1\coding5s_creator_kits
Plantilla base global: C:\...\Student Kit Template.xlsx

Procesando par:
 [Origen]  Coding5s Python Core v0.4 Creator Kit.xlsx
 [Destino] Coding5s Python Core v0.4 Student Kit.xlsx
  [Éxito] Sincronizada correctamente con idioma 'English'.

```


5. **Completion:**
When `Proceso finalizado` appears, press any key to exit. Subfolders now contain localized, standalone **Student Kits** ready for student distribution.

```

```