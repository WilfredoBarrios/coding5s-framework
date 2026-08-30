# 📖 Coding5s Automation Hub — User Guide

## What is Coding5s?
Coding5s is an advanced educational technology framework designed around micro-learning principles, structured to teach programming efficiently through interactive prompts, structured data, and code blocks.

## 🛠️ Module Guide
- **1. Formula Injector:** Injects generation formulas from FGen source tabs into the PromptGenerator sheet. Ensure you select only a single Creator Kit.
- **2. BaseData Updater:** Synchronizes the static BaseData tab across multiple Creator Kits simultaneously. Requires 'creator_kit_Base_File_for_CKs.xlsx' in your Working Directory.
- **3. Student Kit Generator:** Clones global student templates, injects localized language codes into cell B6, formats the data matrix, and secures the workbook.
- **4. Open Files:** A unified file explorer to browse all nested Excel files across subfolders and launch them instantly in Windows Excel, or save a copy to a new location.

## ❓ Frequently Asked Questions (FAQ)
- **Q: Why does my file show as ❌ Missing?**
  A: Ensure the required base template is placed directly in your selected Working Directory, or use the "Find" button to copy it securely.
- **Q: What happens if an Excel file is locked?**
  A: The Hub automatically detects open Excel locks (~$) to prevent corruption errors and safely skips the file with a log warning.