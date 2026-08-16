# 🛠️ Sync Student Kit Generator

The **Sync Student Kit Generator** is an automated compilation and synchronization engine for the **Coding5s** educational framework. It scans the ecosystem's directory structure, reads master source files (**Creator Kits**), and compiles clean, production-ready distribution workbooks (**Student Kits**) without compromising layout integrity, formulas, or formatting.

---

## 💡 Why This Generator Matters

The core vision of **Coding5s** is to empower learners everywhere by making high-quality, prompt-driven programming education accessible worldwide, in any language.

Manually building and updating individual *Student Kits* across dozens of modules and multiple languages is time-consuming and error-prone. This generator solves that problem completely:

* **Global Accessibility & Fast Localization:** Anyone in the world who wants to distribute the **Coding5s** curriculum in their native language (whether it's Swahili, Spanish, French, Japanese, or German) only needs to set their target language in the automation script. Running this tool automatically configures the master *Creator Kits* and compiles a complete, fully localized suite of *Student Kits* ready for deployment.
* **Single Source of Truth:** Creators only need to maintain their content in one place (*Creator Kits*). The generator handles template cloning, language updates, cell mapping, and static value freezing automatically.
* **Scalability:** What used to take hours of manual copy-pasting, formatting, and filter removal now takes minutes across hundreds of course files with a single click.

---

## 🌍 Global Localization Workflow

To localize and publish a full course suite in any language:

1. Open `student_kit_creator.py` in your text editor or IDE.
2. Set the `RESULTS_IN_LANGUAGE` variable to your desired target language (e.g., `"Swahili"`, `"Spanish"`, `"English"`, `"German"`).
3. Save the changes to `student_kit_creator.py`.
4. Run **`Student Kit Creator Runner.bat`**.

The generator will automatically update the language setting across all *Creator Kits*, force Excel to recalculate all prompts, copy the master template (`Template Student Kit.xlsx`), transfer all generated micro-prompts and metadata into static values, clean up layout artifacts, and output ready-to-distribute **Student Kits** configured for that language.

---

## 📂 System Architecture & Components

To run the automated build process, the root folder of your project must contain three core components alongside your localized source folders:

```text
pillar_1/ (Root Directory)
│
├── 📜 Template Student Kit.xlsx     <-- Master visual template
├── 🐍 student_kit_creator.py        <-- Core automation engine
├── ⚙️ Student Kit Creator Runner.bat <-- 1-Click execution script
│
├── 📁 python/                       <-- Language/topic subdirectories
│   ├── Coding5s Python Core... Creator Kit.xlsx
│   └── Coding5s Python Core... Student Kit.xlsx (Automatically generated)
└── 📁 elixir/
    └── ...

```

### 1. `Template Student Kit.xlsx`

The **Master Visual Template**. It contains the clean student layout (`Coding5sStudentKit` and `About` sheets), pre-styled tables, brand colors, and conditional formatting rules.

* **Location:** Must reside in the **root directory**.
* **Role:** Serves as the blueprint. The script never alters this file; instead, it creates a clean clone of it inside each subfolder before injecting localized data.

### 2. `student_kit_creator.py`

The **Core Python Automation Engine**. It orchestrates file discovery, language injection, data extraction, template replication, and desktop-level Excel automation.

* **Key Configuration Variable:**
* `RESULTS_IN_LANGUAGE`: Set this variable at the top of the file to your target language (e.g., `RESULTS_IN_LANGUAGE = "English"`).


* **Modules Used:**
* `os` & `shutil`: Recursive file system navigation and master template cloning.
* `openpyxl`: High-speed memory-based value extraction (`data_only=True`) from localized *Creator Kits*.
* `win32com.client`: Background Windows COM Automation controlling Microsoft Excel. This forces formula recalculation upon language updates and ensures zero corruption of XML table definitions, shapes, or conditional formatting extensions.



### 3. `Student Kit Creator Runner.bat`

The **1-Click Execution Script**. Allows anyone on Windows to run the compilation pipeline with a simple double-click, bypassing the need for a CLI or IDE.

---

## 🔄 How the Build Process Works

When triggered, the engine executes the following 7-step pipeline:

1. **Global Template Validation:**
Verifies the presence of `Template Student Kit.xlsx` in the root folder. Aborts safely if missing.
2. **Recursive Folder Scanning (`os.walk`):**
Scans the root directory and **all subdirectories** (`python`, `elixir`, `gleam`, `dart`, etc.) searching for Excel workbooks containing `"Creator Kit"` in their filename (ignoring active temporary files starting with `~$`).
3. **Language Injection & Recalculation (`win32com`):**
Opens each *Creator Kit* in background Excel, updates cell **B6** on the `PromptGenerator` sheet with the configured `RESULTS_IN_LANGUAGE` value, triggers `excel.Calculate()` to refresh all localized prompt formulas, and saves the file.
4. **Template Cloning (Student Kit Creation):**
For each *Creator Kit* found:
* Calculates the target filename by replacing `"Creator Kit"` with `"Student Kit"`.
* Checks if the *Student Kit* already exists in that specific subfolder.
* If **not present**, clones `Template Student Kit.xlsx` from the root directory into the subfolder and renames it accordingly.


5. **Data Extraction (`openpyxl`):**
Reads the recalculated values from the `PromptGenerator` sheet inside the *Creator Kit*:
* **Main Prompt Matrix:** Range **E9:Y200** (Rows 9–200, Columns 5–25).
* **Header Metadata:** Range **I2:I3** (Module context and language specifications).


6. **Desktop Ingestion (`win32com`):**
Opens the cloned *Student Kit* in background Excel:
* Injects the localized prompt matrix starting at cell **B9**.
* Injects module metadata into range **G2:G3**.
* Disables text wrapping (`WrapText = False`) across modified ranges to prevent layout distortion.
* Clears auto-filters (`AutoFilterMode = False`) for a clean initial view.


7. **Native Save & Integrity Lock:**
Saves the file using Excel’s native file writer—preserving 100% of conditional formatting, cell styles, and table structures—and closes the workbook before proceeding to the next pair.

---

## 🚀 Setup & Requirements

### System Requirements

* **Operating System:** Windows 10/11
* **Software:** Microsoft Excel installed locally
* **Environment:** Python 3.8+

### Dependencies

Open your terminal or command prompt and install the required packages:

```bash
pip install openpyxl pywin32

```

---

## 💻 Step-by-Step Execution

1. **Set the Target Language in the Script:**
Open `student_kit_creator.py` in any text editor, locate the `RESULTS_IN_LANGUAGE` variable at the top, change its value to your preferred language (e.g., `RESULTS_IN_LANGUAGE = "Spanish"`), and save the file.
2. **Verify File Placement:**
Ensure `Student Kit Creator Runner.bat`, `student_kit_creator.py`, and `Template Student Kit.xlsx` are located in your root directory.
3. **Execute the Build:**
Double-click **`Student Kit Creator Runner.bat`**.
4. **Monitor Output:**
The terminal window will display real-time status updates showing language application, template cloning, and synchronization progress:
```text
Iniciando escaneo recursivo en: I:\Github Experiments\coding5s-framework\pillar_1
Plantilla base global: I:\...\Template Student Kit.xlsx

[Creando desde Plantilla Global] Coding5s Python Core v0.4 Student Kit.xlsx
Procesando par:
 [Origen]  Coding5s Python Core v0.4 Creator Kit.xlsx
 [Destino] Coding5s Python Core v0.4 Student Kit.xlsx
  [Éxito] Sincronizada correctamente con idioma 'Spanish'.

```


5. **Completion:**
When the `Proceso finalizado` message appears, press any key to exit. Your subfolders will contain localized, standalone **Student Kits** ready for deployment.

```

```