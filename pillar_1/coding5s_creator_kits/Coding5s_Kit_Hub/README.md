# ️ Coding5s Automation Hub v1.1

**Creator & Student Kit Automation Hub**

[![Version](https://img.shields.io/badge/version-1.1%20Enterprise-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows%2010/11-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.8%2B-yellow.svg)]()

A professional desktop application designed to automate, orchestrate, and scale the generation of AI-powered educational kits for the Coding5s framework.

---

## 🎯 Reason for Being

The Coding5s ecosystem relies on complex Excel workbooks (Creator Kits) to generate structured AI prompts. Managing these kits manually introduces severe operational bottlenecks:
1. **Clipboard & UI Friction:** Manually copying formulas between sheets causes Excel to freeze and leads to formatting errors.
2. **The 8,192 Character Wall:** Excel has a hard limit of 8,192 characters per formula cell. Manual pasting often exceeds this, silently corrupting the workbook.
3. **Localization Scaling:** Generating localized Student Kits for multiple languages requires repetitive, error-prone copy-pasting and manual cell freezing.

The **Automation Hub** eliminates these frictions by replacing manual Excel interaction with a robust, background Windows COM Automation engine, reducing hours of work to seconds while guaranteeing data integrity.

---

## 🛠️ Core Problems Solved

* **Formula Corruption:** Enforces a strict 8,100-character safety limit before injection, preventing Excel buffer overflows.
* **Data Loss:** Implements an **Ephemeral Backup System**. Every file is temporarily backed up before modification and automatically rolled back if an error occurs.
* **UI Freezing:** Executes all Excel operations in an isolated, invisible background process (`DispatchEx`), keeping the UI responsive.
* **Destructive Editing:** The Student Kit Generator extracts data directly into RAM and closes the master Creator Kit *without saving*, leaving the source files 100% pristine.
* **Instance Conflicts:** Uses a Windows Mutex to prevent multiple instances of the Hub from running simultaneously and corrupting files.

---

## ✨ Key Features (The 5 Modules)

###  1. Massive Formula Injector
* **Purpose:** Safely injects generation formulas from calculation sheets (`FGen_S1` to `FGen_S5`) into the master `PromptGenerator` sheet.
* **Workflow:** Selects a **single** Creator Kit via radio buttons.
* **Safety:** Features a real-time character count logger. If a formula exceeds the 8,100 limit, the process aborts instantly and rolls back changes.
* **Resilience:** Includes an anti-saturation retry mechanism that pauses and retries if the background Excel engine is busy.

### 🔄 2. BaseData Mass Updater
* **Purpose:** Synchronizes central rule matrices across multiple Creator Kits simultaneously.
* **Workflow:** Selects **multiple** Creator Kits via checkboxes.
* **Configurability:** Allows dynamic configuration of the Base File, Source Sheet, Copy Range, Target Sheet, and Target Cell.
* **Validation:** Automatically detects if the required Base File is present in the working directory.

###  3. Student Kit Generator & Language Sync
* **Purpose:** Clones global student templates, injects localized content, and generates production-ready Student Kits.
* **Localization Engine:** Integrates `languages.json` to support 15+ languages, including low-resource indigenous languages (Kaqchikel, Mam, Aymara, etc.). Displays language category and spoken regions dynamically.
* **Non-Destructive Extraction:** Opens Creator Kits, updates the language cell, forces recalculation, extracts the prompt matrix to RAM, and closes the file without saving.
* **Output Protection:** Automatically disables text wrapping, clears auto-filters, and applies structural password protection to the generated Student Kits.

### 📂 4. Excel File Explorer (Smart Filter & Multi-Copy)
* **Purpose:** A unified file manager for all generated Kits.
* **Smart Filtering:** Segmented buttons to filter by "All Kits", "Creator Kits", or "Student Kits".
* **Multi-Select Mode:** A toggle switch that changes the UI from single-selection (radio buttons) to batch-selection (checkboxes).
* **Batch Operations:** Allows copying multiple selected files to a destination folder simultaneously.
* **Safety Limits:** Restricts opening a maximum of 3 Excel files at once to prevent system resource exhaustion.

### ❓ 5. Help & Documentation
* **Purpose:** Integrated user guide.
* **Content:** Loads dynamically from `help_content.md`, providing module guides and FAQs.
* **Quick Links:** Direct access to the Official Website, GitHub Framework, and YouTube Tutorials.

---

## ⚙️ Under the Hood: How It Works

### Background COM Automation (`excel_engine.py`)
Instead of interacting with the visible Excel UI, the Hub uses `win32com.client.DispatchEx` to launch an isolated Excel instance.
* `Visible = False`, `ScreenUpdating = False`, `Interactive = False`.
* This prevents UI flickering, avoids stealing window focus, and ensures the user cannot accidentally interrupt the automation.

### Ephemeral Backups & Rollbacks
Before modifying any `.xlsx` file, the engine copies it to the system's temporary directory (`tempfile.gettempdir()`).
* **On Success:** The temporary backup is deleted.
* **On Failure:** The original file on disk is overwritten with the temporary backup, guaranteeing zero data corruption.

### Single-Instance Mutex (`main.py`)
Upon launch, the application registers a global Windows Mutex (`Global\Coding5s_Automation_Hub_Mutex`). If a second instance is launched, it detects the existing lock, displays a native Windows warning, and terminates immediately.

### Portable Path Resolution
The application intelligently detects its environment. If run as a compiled `.exe` (via PyInstaller), it sets the Working Directory to the executable's location. If run from source, it uses the script's directory.

---

## 🚀 Installation & Setup

### Option A: Run from Source (Developers)

**Prerequisites:**
* Windows 10/11
* Python 3.8+
* Microsoft Excel installed locally

**Steps:**
```bash
# 1. Clone the repository
git clone https://github.com/WilfredoBarrios/coding5s-framework.git
cd coding5s-framework/pillar_1/coding5s_creator_kits/Coding5s_Kit_Hub

# 2. Create a virtual environment (optional but recommended)
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install customtkinter pywin32

# 4. Run the application
python main.py
```

### Option B: Run the Executable (End Users)

1. Download the `Coding5s-Hub.exe` from the Releases page.
2. Place the `.exe` in your `coding5s_creator_kits` root directory.
3. Double-click to run. No installation required.

---

## 📂 Project Structure

```text
Coding5s_Kit_Hub/
│
├── 🐍 main.py                 # Entry point & Mutex instance control
├── 🎨 gui_app.py              # CustomTkinter UI layer (5 Tabs, Custom Modals)
├── ️ excel_engine.py         # Windows COM Automation engine & Backup logic
├── 🔧 utils.py                # Filesystem helpers, lock detection, metadata loaders
├── 🌐 languages.json          # Language metadata (Categories & Regions)
├── 📖 about_content.md        # Content for the About modal
├── 📚 help_content.md         # Content for the Help tab
└── 📜 Automation_Hub_Changelog.md  # Version history
```

---

## 📄 License

This project is licensed under the MIT License.
```

***

### 💡 Por qué este README es el correcto:
1. **Cero relleno:** No menciona M2M, Seed Context, ni filosofía pedagógica. Solo habla del software.
2. **Basado en evidencia:** Cada característica mencionada (Mutex, 8100 chars, DispatchEx, Ephemeral Backups, 3-file limit) está escrita directamente en el código que me pasaste.
3. **Estructura profesional:** Sigue el estándar de la industria (Reason for being -> Problems Solved -> Features -> Architecture -> Installation).
4. **Sin predicciones:** No hay sección de "Roadmap" ni "Futuras versiones". Solo describe lo que el Hub **es hoy**.

¿Te gusta así o quieres que ajuste el tono de alguna sección?