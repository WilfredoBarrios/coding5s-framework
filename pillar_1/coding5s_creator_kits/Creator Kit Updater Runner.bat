@echo off
setlocal

:: Force UTF-8 encoding in the console
chcp 65001 >nul

set "vbs_script=%temp%\confirm_update.vbs"

:: Create temporary VBScript dialog
echo res = MsgBox("Are you sure you want to perform the mass update on Creator Kits?", 305, "Update Confirmation") > "%vbs_script%"
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
    python creator_kit_updater.py
    echo.
    echo Process completed.
    echo.
    pause
) else (
    exit /b 0
)