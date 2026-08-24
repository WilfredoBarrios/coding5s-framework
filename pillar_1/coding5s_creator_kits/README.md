# 📚 Coding5s Creator Kits & Automation Infrastructure

Welcome to the **Creator Kits** workspace under **Pillar 1** of the **Coding5s** framework. This directory houses the core engines, templates, and automation tools used to author, scale, and distribute prompt-driven educational content.

---

## 🧠 What are Creator Kits?

**Creator Kits** are master Excel workbooks that act as the central brain for generating the **Coding5s** curriculum.

Inside a Creator Kit, instructors design programming courses broken down into modular stages (`FGen_S1` through `FGen_S5`). Using advanced nested Excel formulas and dynamic variables, these workbooks dynamically compile raw educational inputs (topics, projects, and mentor guidelines) into structured, high-precision AI prompts housed within the `PromptGenerator` sheet. They serve as the **Single Source of Truth** for all programming languages supported in the framework (Python, Elixir, Gleam, Dart, etc.).

---

## 🛠️ The Automation Suite

To eliminate tedious manual work and ensure rapid course scaling, this folder contains three robust Python-powered automation tools, each operated via 1-click Windows batch runners (`.bat`):

### 1. 📋 Formula Auto-Injector (`copy_paster_Prompt_Formulas_for_CK.py`)

* **What it does:** Extracts complex prompt-generation formulas from the modular generation sheets (`FGen_S1` to `FGen_S5`) and batch-injects them directly into the master `PromptGenerator` sheet across all stage ranges (Topics, Projects, Mentors) up to row 200.
* **Why it matters:** Bypasses manual copy-pasting, clipboard wipes, and Notepad text-cleaning. Features a strict **8,100-character safety guard** that instantly aborts and halts execution to protect the workbook if any formula exceeds Excel's native limits.
* **Runner:** `copy_paster_Prompt_Formulas_Runner.bat`

### 2. 🔄 Creator Kit Updater (`creator_kit_updater.py`)

* **What it does:** Performs mass batch updates across all Creator Kits in the directory tree. It reads a central data source (`creator_kit_Base_File_for_CKs.xlsx`) and propagates rule changes or parameters into specific target ranges (e.g., `FGen` rule blocks).
* **Why it matters:** Allows framework architects to update system rules or parameters globally in seconds without disrupting visual styles, conditional formatting, or table structures.
* **Runner:** `Creator Kit Updater Runner.bat`

### 3. 🎓 Sync Student Kit Generator (`student_kit_creator.py`)

* **What it does:** Scans the directory recursively, opens each Creator Kit in background memory (`DispatchEx`), simulates a target language update (e.g., Spanish, English, German) in cell `B6`, recalculates prompts, extracts static values, and compiles clean, protected distribution files (`Student Kits`) using a global visual template (`Student Kit Template.xlsx`).
* **Why it matters:** Enables instant multi-language localization and distribution worldwide while keeping master Creator Kits 100% pristine and untouched (`Close(False)`).
* **Runner:** `Student Kit Creator Runner.bat`

---

## 📂 Directory Structure Overview

```text
coding5s_creator_kits/
│
├── 📁 python/                              <-- Language course subdirectories
├── 📁 elixir/
├── 📁 gleam/
├── 📁 dart/
│
├── 📜 creator_kit_Base_File_for_CKs.xlsx   <-- Central mass-update data source
├── 📜 Student Kit Template.xlsx            <-- Master layout for student distribution
│
├── 🐍 copy_paster_Prompt_Formulas_for_CK.py<-- Tool 1: Formula Auto-Injector
├── ⚙️ copy_paster_Prompt_Formulas_Runner.bat
├── 📖 copy_paster_prompt_formulas_guide.md
│
├── 🐍 creator_kit_updater.py               <-- Tool 2: Mass Rule Updater
├── ⚙️ Creator Kit Updater Runner.bat
├── 📖 creator_kit_guide.md
│
├── 🐍 student_kit_creator.py               <-- Tool 3: Student Kit Generator
├── ⚙️ Student Kit Creator Runner.bat
└── 📖 student_kit_creator_guide.md

```

---

## 🚀 Quick Start Guide

1. **For Formula Injection:** Configure your target file in `copy_paster_Prompt_Formulas_for_CK.py` and run `copy_paster_Prompt_Formulas_Runner.bat`.
2. **For Mass Rule Updates:** Edit `creator_kit_Base_File_for_CKs.xlsx` and run `Creator Kit Updater Runner.bat`.
3. **For Student Kit Compilation:** Set your target language in `student_kit_creator.py` and run `Student Kit Creator Runner.bat`.