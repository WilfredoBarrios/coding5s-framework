# Technical and Functional Documentation: Coding5s Automation Hub

The **Coding5s — Creator & Student Kit Automation Hub** is a modular desktop application developed in Python with a graphical user interface based on CustomTkinter. Its main purpose is to automate repetitive workflows for creating, updating, and synchronizing interactive learning packages in Excel format (*Creator Kits* and *Student Kits*) within the Coding5s educational ecosystem.

---

## 1. Purpose and Problems Solved

### Problems solved:

* **Manual operational overhead:** Eliminates the need to open dozens of Excel files one by one to inject massive formulas, update core data matrices, or generate student versions.
* **Synchronization and format errors:** Standardizes the transfer of complex cell ranges between specific sheets (`PromptGenerator`, `BaseData`, `FGen_S1` to `FGen_S5`, `Coding5sStudentKit`), ensuring the integrity of password-protected structures.


* **Linguistic fragmentation:** Facilitates the mass synchronization of educational content to multiple global languages and low-resource indigenous languages using centralized metadata.


* **Risk of data corruption and locks:** Prevents failures arising from Windows concurrency, files locked by the operating system, uncontrolled openings of Excel instances, or memory saturation on basic computers.



---

## 2. System Architecture

The solution is structured into independent modules that separate the graphical user interface, the Excel automation logic, and support utilities:

* **`main.py`**: Application entry point that implements an exclusion mechanism (Windows *Mutex*) to guarantee the execution of **a single instance** at a time, preventing write conflicts in Excel files.


* **`gui_app.py`**: Manages the dark-themed graphical user interface, tab containers, search bars with quick-clear options, custom modals (`CustomModal`), real-time console redirection (`TextRedirector`), and concurrent thread control (`threading`).


* **`excel_engine.py`**: Automation core using COM (`win32com.client`) to interact invisibly and efficiently with Excel in the background, applying ephemeral backups and retry/rollback systems.


* **`utils.py`**: Provider of helper functions to validate if a file is locked (`is_file_locked`), recursively scan directories, manage user configurations, and resolve static paths compatible with PyInstaller portable environments (`sys._MEIPASS`).


* **`languages.json`**: Internal database with metadata for high-availability languages and indigenous languages (such as K'iche', Kaqchikel, Q'eqchi', Mam, Poqomchi', Tzutujil, etc.).



---

## 3. Detailed Tabs and Functional Features

### Tab 1: 💉 Formula Injector

* **Purpose:** Automate the mass injection of logical formulas extracted from generator sheets (`FGen_S1` to `FGen_S5`) into the central `PromptGenerator` module of a selected *Creator Kit*.


* **Operation:** Scans and processes a predefined cell map (for example, source ranges like `E3:E50` to destination columns like `K` with a row limit up to `200`).


* **Validations:** Evaluates that the formula text does not exceed the strict limit of **8,100 characters**. If exceeded, the task safely halts.



### Tab 2: 🔄 BaseData Updater

* **Purpose:** Mass-synchronize central core data from a base file to multiple *Creator Kits*.


* **Operation:** Reads a configured data matrix (by default from the `creator_kit_Base_File_for_CKs.xlsx` file, `BaseData` sheet, range `A1:B10`) and injects it into the target cell (for example, `C95` in the `FGen_S1` sheet) of all selected kits.



### Tab 3: 🎓 Student Kit Generator & Language Sync

* **Purpose:** Automatically generate student study packages (*Student Kits*) from a global template and adapt them to the selected language.


* **Operation:**
* Uses `Student Kit Template.xlsx` as the base.


* Updates cell `B6` of the creator with the specified target language and recalculates values.


* Extracts data blocks from `E9:Y200` and metadata `I2:I3` from the *Creator Kit* and transfers them to the `Coding5sStudentKit` sheet of the *Student Kit*.


* Manages sheet structure protection via the internal configured password (`wil`).





### Tab 4: 📂 Open Files (Excel Explorer)

* **Purpose:** Act as an intelligent explorer within the working directory for visual management and quick file manipulation.


* **Filters and Search:** Allows quick toggling between views (*All Kits*, *Creator Kits*, *Student Kits*) and filtering files via a text box with a dedicated quick-clear button (`✖`).


* **Multi-Select and Security:** When activating the *Multi-Select Mode* switch, it enables block selection controls (*Select All* / *Deselect All*) and allows massive copying to external directories.


* **Opening Limit:** Incorporates a safety protection mechanism that restricts simultaneous opening in Excel to a **maximum of 3 files at a time**, disabling the button and showing visual warnings if this threshold is exceeded to prevent freezes on basic computers.



### Tab 5: ❓ Help & About

* **Purpose:** Provide internal help documentation and informative shortcuts regarding the framework and project links.



---

## 4. Security and Performance Mechanisms

* **Single Instance Control (Mutex):** Uses the Windows API via `ctypes` to verify if the Hub is already running; if so, it issues a native warning and prevents opening duplicate processes that could overlap disk writes.


* **Dynamic Root Directory:** Configured by default to recognize and set the exact folder where the portable executable is hosted as the working path, facilitating its distribution to teachers in different environments without relying on absolute paths.


* **Transactional Handling with Ephemeral Backup:** Before modifying any Excel file, the engine creates a temporary backup copy (`tempfile`). If a critical error occurs or an integrity rule is violated, the system automatically performs a rollback restoring the original file.


* **Robust Packaging:** Compatible with PyInstaller (`--onefile --noconsole`), securely integrating necessary internal static resources (`languages.json`, markdown help files) via temporary execution directory handling (`_MEIPASS`).