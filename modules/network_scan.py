import socket
import json
import os
from scapy.all import ARP, Ether, srp

# Set correct path for known_devices.json
DEVICE_LOG_PATH = os.path.join("..", "logs", "known_devices.json")

def scan_network(ip_range="192.168.1.0/24"):
    """ Scan the network for connected devices """
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request
    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'hostname': get_hostname(received.psrc)
        })

    return devices

def get_hostname(ip):
    """ Get hostname from IP """
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def get_known_devices():
    """ Load known devices from JSON file """
    if os.path.exists(DEVICE_LOG_PATH):
        with open(DEVICE_LOG_PATH, "r") as file:
            return json.load(file)
    return []

def save_known_devices(devices):
    """ Save connected devices to JSON file """
    with open(DEVICE_LOG_PATH, "w") as file:
        json.dump(devices, file, indent=4)

if __name__ == "__main__":
    devices = scan_network()
    
    # Load existing devices and check for new ones
    known_devices = get_known_devices()
    new_devices = [d for d in devices if d not in known_devices]

    if new_devices:
        print("🚨 New Device(s) Detected! Updating Log.")
        save_known_devices(devices)
    
    print(devices)
