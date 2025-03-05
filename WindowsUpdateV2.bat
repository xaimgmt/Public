@echo off
powershell -Command "Install-Module -Name PSWindowsUpdate -Force"
powershell -Command "Get-WindowsUpdate"
powershell -Command "Install-WindowsUpdate"
powershell -Command "Get-WindowsUpdate -AcceptAll -Install -AutoReboot"
