
import sys
sys.path.append(r'\\10.234.219.222\Py$\Lib')
import pyautogui
import time
import pygetwindow as gw
import os
os.system('cls')

def s(detik):
    time.sleep(detik)

def WinClick(nama_jendela, koordinat_X, koordinat_Y):
    window = gw.getWindowsWithTitle(nama_jendela)
    if window:
        window = window[0]
        if window.isMinimized:
            window.restore()
        window.activate()
        time.sleep(0.5)
        x, y = window.left + koordinat_X, window.top + koordinat_Y
        pyautogui.click(x, y)

def WinGetColor(nama_jendela, koordinat_X, koordinat_Y, kode_warna):
    window = gw.getWindowsWithTitle(nama_jendela)
    if window:
        window = window[0]
        if window.isMinimized:
            window.restore()
        window.activate()
        time.sleep(0.5)
        x, y = window.left + koordinat_X, window.top + koordinat_Y
        screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
        color = screenshot.getpixel((0, 0))
        return color == kode_warna
    else:
        raise Exception(f"Jendela dengan nama '{nama_jendela}' tidak ditemukan.")

# ====================================================================================================

s(0.5); pyautogui.hotkey('win', 'left')
s(0.5); pyautogui.hotkey('esc')
s(0.5); pyautogui.hotkey('win', 'home')

s(0.5); pyautogui.hotkey('win', 'e')
s(0.5); pyautogui.hotkey('win', 'right')
s(0.5); pyautogui.hotkey('esc')
s(0.5); pyautogui.hotkey('alt', 'd')
s(0.5); pyautogui.typewrite('This PC')
s(0.5); pyautogui.hotkey('enter')

CN = os.environ.get('COMPUTERNAME')
if CN == 'PMIIDIDNW03648':
    LokasiFileISO = 'A:\\ISO\\Original\\WipeOri11 2505 for User.iso'
    DriveLast = 'X'
elif CN == 'PMIIDIDNW04472':
    LokasiFileISO = 'A:\\ISO\\WipeOri11 2503 for User.iso'
    DriveLast = 'Z'

os.system(f'start "" /min C:\\ProgramData\\rufus-4.9.exe -i "{LokasiFileISO}" -f NTFS')
s(5)

versi_rufus = 'Rufus 4.9.2256'
for i in range(10):
    print(i + 1, end=' ')
    while True:
        if WinGetColor(versi_rufus, 95, 442, (6, 176, 37)):
            WinClick(versi_rufus, 412, 486) # CANCEL
            s(1); WinClick('Rufus - Cancellation', 268, 137)
            s(1); WinClick('Cancelled', 407, 124)
            s(3); WinClick(versi_rufus, 238, 103) # Device
            s(1); pyautogui.hotkey('down') # Pilih USB
            s(1); pyautogui.hotkey('enter') # Enter
            s(1)
            break

        if WinClick('Error', 402, 124):
            sys.exit()

        WinClick(versi_rufus, 306, 488) # START
        WinClick('Revoked UEFI bootloader detected', 276, 243)
        WinClick('Rufus', 277, 150)
        WinClick('Rufus - Cancellation', 268, 137)
        WinClick('Cancelled', 407, 124)

        time.sleep(1)

s(3); os.system('taskkill /f /im rufus-4.9.exe')

for i in range(5):
    os.system(f"powershell Dismount-DiskImage -ImagePath '{LokasiFileISO}'")

os.system(f"powershell Mount-DiskImage -ImagePath '{LokasiFileISO}'")
for drive_letter in range(ord('D'), ord(DriveLast) + 1):
    if os.path.exists(f"{chr(drive_letter)}:\\WINSETUP\\Win11\\Windows11.iso"):
        Src = chr(drive_letter)

for drive_letter in range(ord('D'), ord(DriveLast) + 1):
    if os.path.exists(f"{chr(drive_letter)}:\\WINSETUP"):
        Des = chr(drive_letter)
        if Des != Src:
            os.system(f'title Refill FD Wipe Ori - Src {Src}: Des {Des}: & color e & robocopy /mir {Src}:\\ {Des}:\\')

sys.exit()

