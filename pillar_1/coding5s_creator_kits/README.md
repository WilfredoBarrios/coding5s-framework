# 📚 Coding5s Creator Kits & Automation Infrastructure

Welcome to the **Creator Kits** workspace under **Pillar 1** of the **Coding5s** framework. This directory houses the core engines, templates, and automation tools used to author, scale, and distribute prompt-driven educational content.

---

##  What's New: Automation Hub v1.1

**🚀 The Future of Course Creation is Here!**

This directory now includes the **Coding5s Automation Hub** (`Coding5s-Hub.exe`), a professional desktop application that unifies all automation tools into a single, intuitive graphical interface.

**Why Use the Hub?**
- **No Coding Required:** Run complex automations with clicks, not terminal commands.
- **Visual Feedback:** Real-time logs, progress bars, and safety confirmations.
- **Smart File Management:** Built-in explorer with multi-copy, filtering, and batch operations.
- **Global Localization:** Generate Student Kits in 15+ languages (including indigenous languages) with one click.
- **Safety First:** Automatic backups, file lock detection, and 8,100-character validation.

👉 **To get started:** Simply double-click `Coding5s-Hub.exe`. No installation required!

---

## 🧠 What are Creator Kits?

**Creator Kits** are master Excel workbooks that act as the central brain for generating the **Coding5s** curriculum.

Inside a Creator Kit, instructors design programming courses broken down into modular stages (`FGen_S1` through `FGen_S5`). Using advanced nested Excel formulas and dynamic variables, these workbooks dynamically compile raw educational inputs (topics, projects, and mentor guidelines) into structured, high-precision AI prompts housed within the `PromptGenerator` sheet. They serve as the **Single Source of Truth** for all programming languages supported in the framework (Python, Elixir, Gleam, Dart, etc.).

---

## ️ Automation Tools

The Automation Hub provides a GUI for these three core engines. For advanced users, the original Python scripts and batch runners are still available in the `automation_scripts_legacy_backup` folder.

### 1. 💉 Formula Auto-Injector
* **What it does:** Extracts complex prompt-generation formulas from modular generation sheets (`FGen_S1` to `FGen_S5`) and batch-injects them directly into the master `PromptGenerator` sheet across all stage ranges (Topics, Projects, Mentors) up to row 200.
* **Why it matters:** Bypasses manual copy-pasting, clipboard wipes, and Notepad text-cleaning. Features a strict **8,100-character safety guard** that instantly aborts execution if any formula exceeds Excel's native limits.
* **Access:** Use **Tab 1** in the Automation Hub.

### 2.  BaseData Mass Updater
* **What it does:** Performs mass batch updates across all Creator Kits in the directory tree. It reads a central data source (`creator_kit_Base_File_for_CKs.xlsx`) and propagates rule changes or parameters into specific target ranges (e.g., `FGen` rule blocks).
* **Why it matters:** Allows framework architects to update system rules or parameters globally in seconds without disrupting visual styles, conditional formatting, or table structures.
* **Access:** Use **Tab 2** in the Automation Hub.

### 3. 🎓 Student Kit Generator & Language Sync
* **What it does:** Scans the directory recursively, opens each Creator Kit in background memory (`DispatchEx`), simulates a target language update in cell `B6`, recalculates prompts, extracts static values, and compiles clean, protected distribution files (`Student Kits`) using a global visual template (`Student Kit Template.xlsx`).
* **Why it matters:** Enables instant multi-language localization and distribution worldwide while keeping master Creator Kits 100% pristine and untouched (`Close(False)`).
* **Access:** Use **Tab 3** in the Automation Hub.

### 4.  Excel File Explorer (NEW!)
* **What it does:** A built-in file manager with smart filtering (All Kits / Creator Kits / Student Kits), search capabilities, and batch operations.
* **Why it matters:** Copy multiple files at once, open files directly in Excel (max 3 at a time for safety), and manage your entire course library without leaving the app.
* **Access:** Use **Tab 4** in the Automation Hub.

---

## 📂 Directory Structure Overview

```text
coding5s_creator_kits/
│
├── 🚀 Coding5s-Hub_v1.1.exe          <-- 🌟 MAIN APPLICATION (Double-click to run!)
│
├── 📁 python/                          <-- Language course subdirectories
├── 📁 elixir/
├── 📁 gleam/
├── 📁 dart/
│
├── 📜 creator_kit_Base_File_for_CKs.xlsx   <-- Central mass-update data source
├── 📜 Student Kit Template.xlsx            <-- Master layout for student distribution
│
├── 📁 Coding5s_Kit_Hub/                    <-- Hub source code & documentation
│   ├──  main.py
│   ├── 🎨 gui_app.py
│   ├── ⚙️ excel_engine.py
│   ├── 🔧 utils.py
│   ├── 🌐 languages.json
│   └── 📚 Documentation files (.md)
│
└── 📁 automation_scripts_legacy_backup/    <-- Original Python scripts & .bat runners
    ├──  copy_paster_Prompt_Formulas_for_CK.py
    ├── 🐍 creator_kit_updater.py
    ├── 🐍 student_kit_creator.py
    └── ⚙️ *.bat (Runner scripts)
```

---

##  Quick Start Guide

### **Option A: Using the Automation Hub (Recommended)**

1. **Launch the App:** Double-click `Coding5s-Hub_v1.1.exe`.
2. **Navigate the Tabs:**
   - **Tab 1 (Formula Injector):** Select a Creator Kit and click "Inject Formulas".
   - **Tab 2 (BaseData Updater):** Select multiple kits and click "Update Selected Kits".
   - **Tab 3 (Student Kit Generator):** Choose a language, select kits, and click "Generate Student Kits".
   - **Tab 4 (File Explorer):** Browse, filter, and copy your files.
3. **Monitor Progress:** Watch real-time logs in the bottom panel of each tab.

### **Option B: Using Legacy Scripts (Advanced)**

For users who prefer command-line execution or need to customize the automation logic:

1. **Formula Injection:**
   - Edit `automation_scripts_legacy_backup/copy_paster_Prompt_Formulas_for_CK.py` to set your target file.
   - Run `copy_paster_Prompt_Formulas_Runner.bat`.

2. **Mass Updates:**
   - Edit `creator_kit_Base_File_for_CKs.xlsx` with your new rules.
   - Run `Creator Kit Updater Runner.bat`.

3. **Student Kit Generation:**
   - Edit `automation_scripts_legacy_backup/student_kit_creator.py` to set `RESULTS_IN_LANGUAGE`.
   - Run `Student Kit Creator Runner.bat`.

---

##  Documentation & Resources

- **Hub Documentation:** Inside the app, click **Tab 5 (Help)** for a complete user guide.
- **Script Guides:** Detailed technical documentation for each automation script is available in the `automation_scripts_legacy_backup` folder.
- **Framework Overview:** Visit [coding5s.com](https://coding5s.com) or check the main repository README.

---

## 🌍 Supported Languages

The Automation Hub supports localization for 15+ languages out of the box:

**High-Resource Languages:** English, Spanish, French, German, Portuguese

**Low-Resource Indigenous Languages:** K'iche', Kaqchikel, Q'eqchi', Mam, Poqomchi', Tz'utujil, Nahuatl, Quechua, Aymara, Guarani

*(Language metadata is managed via `languages.json` inside the Hub source folder)*

---

## ⚙️ System Requirements

- **Operating System:** Windows 10/11
- **Software:** Microsoft Excel (required for COM Automation)
- **For Hub Users:** No Python installation needed (the `.exe` is portable).
- **For Script Users:** Python 3.8+ and `pip install pywin32 customtkinter`.

---

<div align="center">

**Built with ❤️ for the Coding5s Community**

*Empowering education through controlled cognitive friction.*

</div>