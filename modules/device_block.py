import os

def block_unknown_device(mac_address):
    """ Block an unknown MAC address from the network """
    block_command = f"netsh wlan add filter permission=denyall ssid=YourNetwork MAC={mac_address}"
    os.system(block_command)
    print(f"🚨 Unauthorized Device Blocked: {mac_address}")

if __name__ == "__main__":
    test_mac = "AA:BB:CC:DD:EE:FF"
    block_unknown_device(test_mac)
# Replace "YourNetwork" with your actual WiFi SSID.