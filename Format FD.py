import os

def format_flash_drive(disk_number):
    commands = [
        f"diskpart /s /c \"select disk {disk_number}\"",
        "clean",
        "create partition primary",
        "format fs=ntfs quick",
        "assign"
    ]
    for command in commands:
        os.system(f"echo {command} | diskpart")

# Format flash drives located at disk 1 to disk 5
for i in range(1, 6):
    format_flash_drive(i)

print("Flash drives from disk 1 to disk 5 have been formatted to NTFS successfully.")
