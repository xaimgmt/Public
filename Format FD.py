
import os
import time
import psutil
import sys
os.system("cls")

def detect_udf_drives():
    udf_drives = []
    for partition in psutil.disk_partitions():
        if partition.fstype.lower() == "udf":
            udf_drives.append(partition.device)
    return udf_drives

udf_drives = detect_udf_drives()
udf_drives_str = ", ".join(udf_drives).replace("['", "").replace("']", "")
print("UDF Drives Detected:", udf_drives_str)
# sys.exit()

def format_flash_drive(disk_number):
    commands = [
        f"select disk {disk_number}",
        "clean",
        "create partition primary",
        "format fs=ntfs quick",
        "assign",
        "active"
    ]
    script_path = "C:\\Temp\\dp.txt"
    with open(script_path, "w") as script_file:
        script_file.write("\n".join(commands))
    os.system(f"diskpart /s {script_path}")

# Format flash drives located at disk 1 to disk 5
for i in range(1, 6):
    format_flash_drive(i)

time.sleep(3)

for i in range(1, 6):
    format_flash_drive(i)

for drive_letter in range(ord('D'), ord('P') + 1):
    if chr(drive_letter) == 'D':
        continue
    # os.system(f'robocopy /mir C: {chr(drive_letter)}:')
    os.system(f'robocopy /mir {udf_drives_str}\ {chr(drive_letter)}:\\')

# for drive_letter in ['E', 'G', 'I', 'K']:
#     os.system(f'robocopy /mir D: {drive_letter}:')

print("DONE")

