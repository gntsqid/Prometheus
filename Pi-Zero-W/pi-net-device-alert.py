from scapy.all import ARP, sniff
import json
import socket

# Dictionary to store known devices
known_devices = {}

def get_host_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def handle_packet(packet):
    if packet.haslayer(ARP):
        if packet[ARP].op == 2:  # Only ARP Replies
            ip = packet[ARP].psrc
            mac = packet[ARP].hwsrc
            status = "Recognized" if mac in known_devices else "New"
            hostname = get_host_name(ip) if status == "New" else known_devices[mac]['hostname']
            known_devices[mac] = {'ip': ip, 'hostname': hostname}
            device_info = {
                'Device': {
                    'Status': status,
                    'ip': ip,
                    'MAC': mac,
                    'hostname': hostname
                }
            }
            print(json.dumps(device_info, indent=5))

# Run the packet sniffer on the network interface connected to the network
def run_sniffer(interface="wlan0"):
    sniff(prn=handle_packet, filter="arp", store=0, iface=interface)

# Example usage: Adjust the interface as needed
run_sniffer("wlan0")  # For WiFi, or "eth0" for Ethernet

# NOTE: DOESNT WORK I DONT THINK