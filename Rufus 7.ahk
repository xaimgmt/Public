
Source := 'M'
loop 2
{
    WinActivate('Rufus', 'Cluster')
    ControlFocus('ComboBox1', 'Rufus', 'Cluster') ; Device
    if A_Index = 1 {
        Send('{Home}')
    } else {
        Send('{Home}')
        n := A_Index - 1
        Send('{Down ' n '}') ; Select device
    }
    ControlClick('Button14', 'Rufus', 'Cluster') ; START
    Cek_Popup()
}
Loop 20  ; D sampai X = 20 huruf
{
    Destination := Chr(Ord("D") + A_Index - 1) ":"
    if DirExist(Destination "\WINSETUP")
    {
        if (Destination != Source ":")
        {
            RunWait A_ComSpec " /c ROBOCOPY /MIR " Source ": " Destination
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
        } else if WinExist('Error', 'another process') {
            ControlClick('Button1', 'Error', 'another process')
        } else if WinExist('Rufus', 'WARNING') {
            ControlClick('Button1', 'Rufus', 'WARNING')
        } else if WinExist('Revoked UEFI bootloader detected') {
            ControlClick('Button1', 'Revoked UEFI bootloader detected')
        }
        Sleep(1000) ; Loop lebih stabil
    }
}

