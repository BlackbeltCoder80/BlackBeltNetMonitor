from modules.network_scan import scan_network, get_known_devices, save_known_devices
from modules.device_block import block_unknown_device
from modules.http_logger import capture_http_requests
from modules.dns_logger import start_dns_sniffing
from modules.alert_system import send_alert

def main():
    print("🚀 Network Monitoring Started!")

    # Scan devices on the network
    devices = scan_network()
    print(f"📡 Detected Devices: {devices}")

    # Load existing known devices and check for new ones
    known_devices = get_known_devices()
    new_devices = [d for d in devices if d not in known_devices]

    if new_devices:
        print("🚨 New Device(s) Detected! Updating Log.")
        save_known_devices(devices)

        # Optionally block new devices
        for device in new_devices:
            block_unknown_device(device["mac"])

    # Start logging HTTP & DNS traffic
    capture_http_requests()
    start_dns_sniffing()

if __name__ == "__main__":
    main()

