# Coding5s Automation Hub Changelog

## Version 1.1 (August 2026)

* Added **Excel File Explorer (Smart Filter & Multi-Copy)** tab allowing users to filter files by type ("All Kits", "Creator Kits", "Student Kits"), search files dynamically, and copy multiple files simultaneously.


* Added **Multi-Select Mode** toggle with individual checkbox controls and bulk "Select All" / "Deselect All" capabilities across the file management interface.


* Added a safety limit to prevent opening more than 3 Excel files simultaneously in the explorer tab, protecting low-resource systems from freezing or crashing.


* Integrated **CustomTkinter Modal dialogs** to replace native Windows alert boxes for cleaner styling and better user feedback.


* Added **Localization & Language Metadata support**, allowing synchronization with diverse global and low-resource indigenous languages via `languages.json`.


* Implemented single-instance application control via a Windows Mutex lock to prevent simultaneous multi-instance execution conflicts.


* Optimized portability: the application now automatically detects and sets its working directory to the executable's path on startup.


* Embedded internal static assets (`languages.json`, `about_content.md`, `help_content.md`) securely inside the compiled package using PyInstaller `_MEIPASS` handling.



---

## Version 1.0 (Initial Release)

* Initial release of **Coding5s — Creator & Student Kit Automation Hub**.


* **Massive Formula Injector**: Automated extraction and insertion of template generation formulas from calculation sheets into the `PromptGenerator` module across selected Creator Kits.


* **BaseData Mass Updater**: Synchronized central core matrix definitions from `creator_kit_Base_File_for_CKs.xlsx` into `FGen_S1` across multiple targeted Creator Kits.


* **Student Kit Generator & Language Sync**: Automated generation of student execution packages derived from `Student Kit Template.xlsx`, embedding localized strings and custom protection schemas.


* **Modular Architecture & UI**: Built with a clean Dark-themed CustomTkinter graphical interface, featuring real-time threaded execution logs via `TextRedirector`.


* Recursive directory scanning to locate nested `.xlsx` Creator Kits across custom folder structures.