
import sys
sys.path.append('C:\\Program Files\\Python313\\Lib')
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

versi_rufus = 'Rufus 4.9.2256'
for i in range(2):
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

        WinClick(versi_rufus, 306, 488) # START
        WinClick('Revoked UEFI bootloader detected', 276, 243)
        WinClick('Rufus', 277, 150)
        WinClick('Rufus - Cancellation', 268, 137)
        WinClick('Cancelled', 407, 124)

        time.sleep(1)

    