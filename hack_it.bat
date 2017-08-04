@echo off
set PORT=%1
if "%PORT%" == "" (
    set PORT=5000
)
python chew_toy_web %PORT%
