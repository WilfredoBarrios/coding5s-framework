# 🛠️ Sync Creator Kit Updater

The **Sync Creator Kit Updater** is a batch synchronization engine designed for the **Coding5s** educational framework. It scans the ecosystem's directory structure, reads static configurations or rule matrices from a central master source (`creator_kit_Base_File_for_CKs.xlsx`), and updates specific ranges across all **Creator Kits** without altering visual formatting, conditional styles, or existing formulas.

---

## 💡 Why This Updater Matters

In the **Coding5s** framework, *Creator Kits* serve as the core engines for prompt generation. As instructional rules, system prompts, or core framework parameters evolve, manually propagating these changes across dozens of *Creator Kits* across various programming languages (`python`, `elixir`, `gleam`, `dart`) becomes an operational bottleneck.

This updater solves that problem completely:

* **Mass Parameter Propagation:** Allows framework architects to update system rules, prompt formulas, or atomic guidelines across the entire library in seconds rather than spending hours opening and editing files manually.
* **Format-Preserving Ingestion:** By transferring static matrix values directly via Windows COM Automation (`rango_destino.Value = matriz_valores`), it injects new rules while leaving visual styles, fonts, cell borders, and conditional formatting rules 100% intact.


* **Automatic Recalculation:** Forces a global recalculation (`excel.Calculate()`) immediately after injection, ensuring all dependent formulas inside the *Creator Kits* instantly adapt to the updated rules.


* **Single Source of Truth:** Centralizes framework updates into one master file (`creator_kit_Base_File_for_CKs.xlsx`).



---

## ⚙️ Target Matrix Configuration

To define what data gets copied and where it lands, update the configuration block at the top of `creator_kit_updater.py`:

```python
# ==========================================
# ⚙️ MAIN CONFIGURATION VARIABLES
# ==========================================
ARCHIVO_BASE_NOMBRE = "creator_kit_Base_File_for_CKs.xlsx"
PESTANA_BASE_ORIGEN = "BaseData"           # Source sheet in the base file
RANGO_A_COPIAR = "A1:B10"                  # Cell range to extract from base file

PESTANA_DESTINO_CK = "FGen_S1"             # Target sheet in Creator Kits
CELDA_INICIAL_DESTINO = "C95"              # Starting top-left cell for destination paste
# ==========================================
```[cite: 8]

---

## 📂 System Architecture & Components

To run the batch update process, the `coding5s_creator_kits` directory (under Pillar 1) must contain these core files alongside topic subdirectories:

```text
pillar_1/coding5s_creator_kits/
│
├── 📜 creator_kit_Base_File_for_CKs.xlsx <-- Central data/rules source
├── 🐍 creator_kit_updater.py              <-- Core Python automation engine
├── ⚙️ Creator Kit Updater Runner.bat      <-- 1-Click execution script
├── 📖 README.md                           <-- Documentation
│
├── 📁 python/                             <-- Language/topic subdirectories
│   └── Coding5s Python Core... Creator Kit.xlsx
├── 📁 elixir/
├── 📁 gleam/
└── 📁 dart/

```

### 1. `creator_kit_Base_File_for_CKs.xlsx`

The **Central Master Source File**. Holds the updated rules, system parameters, or formulas on the sheet defined by `PESTANA_BASE_ORIGEN`.

* **Location:** Must reside in the same root folder as `creator_kit_updater.py`.


* **Role:** Acts as the data donor. The script extracts static values from `RANGO_A_COPIAR` and propagates them across all *Creator Kits*.



### 2. `creator_kit_updater.py`

The **Core Python Automation Engine**. Manages recursive file discovery, COM Excel background instantiation, array dimension mapping, static value injection, and recalculation triggers.

* **Key Dependencies:** `os`, `win32com.client`.



### 3. `Creator Kit Updater Runner.bat`

The **1-Click Execution Script**. Launches a native VBScript confirmation dialog before executing the update engine, preventing accidental mass overwrites.

---

## 🔄 How the Update Process Works

When executed, the script follows a 5-step pipeline:

1. **Master Source Validation:**
Verifies that `creator_kit_Base_File_for_CKs.xlsx` exists in the root folder. If missing, execution halts immediately with a critical error log.


2. **Recursive Search (`os.walk`):**
Scans the root folder and **all subdirectories** (`python`, `elixir`, `gleam`, `dart`, etc.) to locate all `.xlsx` workbooks containing `"Creator Kit"` in their filename (excluding temporary active files `~$` and the base file itself).


3. **Master Matrix Extraction:**
Launches background Excel COM Automation (`win32com.client.Dispatch("Excel.Application")`), opens the base file, reads `RANGO_A_COPIAR` as a 2D array into RAM memory, and immediately closes the base file.


4. **Batch Ingestion & Recalculation:**
Iterates through each discovered *Creator Kit*:
* Opens the file in background Excel.


* Dynamically calculates target range dimensions based on the shape of the source matrix.


* Overwrites target cell values (`rango_destino.Value = matriz_valores`) without touching formatting.


* Forces a full workbook recalculation (`excel.Calculate()`).


* Saves and closes the *Creator Kit* (`wb_ck.Close(True)`).




5. **Memory Cleanup:**
Ensures all COM objects are released, screen updating and alert modes are restored, and Excel instances are safely terminated in the `finally` block.



---

## 🚀 Setup & Requirements

### System Requirements

* **Operating System:** Windows 10/11
* **Software:** Microsoft Excel installed locally
* **Environment:** Python 3.8+

### Dependencies

Install the required Windows COM library via terminal:

```bash
pip install pywin32

```

---

## 💻 Step-by-Step Execution

1. **Configure Update Variables:**
Open `creator_kit_updater.py` in your text editor. Adjust `PESTANA_BASE_ORIGEN`, `RANGO_A_COPIAR`, `PESTANA_DESTINO_CK`, and `CELDA_INICIAL_DESTINO` according to the update requirements, then save.


2. **Prepare Data Source:**
Place the new rules or parameters in `creator_kit_Base_File_for_CKs.xlsx` inside the specified range.


3. **Execute the Batch Update:**
Double-click **`Creator Kit Updater Runner.bat`**. Confirm the action in the prompt dialog.


4. **Monitor Console Progress:**
The command window will log real-time updates:
```text
Iniciando proceso de actualización masiva...
Directorio raíz: C:\github_repositories\coding5s-framework\pillar_1\coding5s_creator_kits
Archivo base: C:\...\creator_kit_Base_File_for_CKs.xlsx

Se encontraron 4 Creator Kits para actualizar.
Cargando valores desde 'BaseData' (Rango: A1:B10)...
Matriz cargada con éxito. Aplicando actualizaciones en lote...

Procesando: Coding5s Python Core v0.4 Creator Kit.xlsx
  [Éxito] Datos pegados y fórmulas recalculadas.

```


5. **Completion:**
Once finished, press any key to exit. All *Creator Kits* now contain the updated rules and refreshed formulas.