@echo off
setlocal

:: Force UTF-8 encoding in the console
chcp 65001 >nul

set "vbs_script=%temp%\confirm_update.vbs"

:: Create temporary VBScript dialog
echo res = MsgBox("Are you sure you want to copy and paste all the formulas in the Stages? Remember, this script will copy the generated formulas from the five FGen_S# sheets of the Excel file that you specified in the copy_paster_Prompt_Formulas.py file, and then paste them into the PromptGenerator sheet, in their respective cells, extending the formulas as needed.", 305, "Update Confirmation") > "%vbs_script%"
echo WScript.Quit(res) >> "%vbs_script%"

:: Execute prompt and capture output
cscript //nologo "%vbs_script%"
set "user_choice=%errorlevel%"

:: Clean up temporary file
del "%vbs_script%" >nul 2>&1

:: Evaluate response: 1 = OK, 2 = Cancel
if "%user_choice%"=="1" (
    echo.
    echo Running synchronization script...
    python copy_paster_Prompt_Formulas_for_CK.py
    echo.
    echo Process completed.
    echo.
    pause
) else (
    exit /b 0
)