
@echo off
cls
robocopy /IS "C:\Users\Saif\OneDrive\Software\Artwork\PY" %ProgramData% Rufus.py
start "" "C:\Program Files\Python313\python.exe" %ProgramData%\Rufus.py
cls

