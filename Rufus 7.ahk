
Run('B:\Software\rufus-4.9.exe -i "A:\ISO\Original\WipeOri11 2505 for User.iso" -f NTFS')
WinWaitActive('Rufus', 'Cluster')

Source := 'W' ; Ganti dengan Drive mount file ISO
Label := 'WipeOri11 2505 for User'
loop 10
{
    WinActivate('Rufus', 'Cluster')
    ControlFocus('ComboBox1', 'Rufus', 'Cluster') ; Device
    if A_Index = 1 {
        Send('{Home}')
    } else {
        Send('{Home}')
        Sleep(200)
        n := A_Index - 1
        loop n
        {
            Send('{Down}') ; Select device
            Sleep(200)
        }
    }
    ControlClick('Button14', 'Rufus', 'Cluster') ; START
    Cek_Popup()
}
WinMinimizeAll
WinClose('Rufus', 'Cluster')
Loop 20  ; D sampai X = 20 huruf
{
    Destination := Chr(Ord("D") + A_Index - 1) ":"
    if DirExist(Destination "\WINSETUP")
    {
        if (Destination != Source ":")
        {
            RunWait A_ComSpec " /c Label Destination " Label
            RunWait A_ComSpec " /c ROBOCOPY /MIR " Source ": " Destination, , 'Min'
        }
    }
}
ExitApp

Cek_Popup()
{
    loop
    {
        v1 := ControlGetText('msctls_progress321', 'Rufus', 'Cluster')
        if WinExist('Cancelled', 'cancelled') {
            ControlClick('Button1', 'Cancelled', 'cancelled')
            return
        } else if WinExist('Rufus - Cancellation', 'Cancelling') {
            ControlClick('Button1', 'Rufus - Cancellation', 'Cancelling')
        } else if InStr(v1,'Copying ISO') {
            Sleep(10000)
            ControlClick('Button15', 'Rufus', 'Cluster') ; CANCEL
        } else if WinExist('GB]', 'Another program') {
            ControlClick('Button3', 'GB]', 'Another program')
        } else if WinExist('Error', 'another process') {
            ControlClick('Button1', 'Error', 'another process')
        } else if WinExist('Rufus', 'WARNING') {
            ControlClick('Button1', 'Rufus', 'WARNING')
        } else if WinExist('Revoked UEFI bootloader detected') {
            ControlClick('Button1', 'Revoked UEFI bootloader detected')
        }
        Sleep(1000) ; Loop lebih stabil
        if (A_Index == 60) {
            return
        }
    }
}

