@echo off
setlocal

:: Force UTF-8 encoding in the console
chcp 65001 >nul

set "vbs_script=%temp%\confirm_update.vbs"

:: Create temporary VBScript dialog
echo res = MsgBox("Are you sure you want to create all the Student Kits? Remember, this script will look for all Excel files that contain the words (Creator Kit) in their names, and then it will create their respective Student Kits in the language that you set in the student_kit_creator.py file.", 305, "Update Confirmation") > "%vbs_script%"
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
    python student_kit_creator.py
    echo.
    echo Process completed.
    echo.
    pause
) else (
    exit /b 0
)