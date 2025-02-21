from scapy.all import sniff
import datetime

def capture_http_requests():
    """ Capture HTTP requests to log visited pages. """
    print("🌍 Capturing HTTP Requests...")
    sniff(filter="tcp port 80", prn=log_http_request, store=0)

def log_http_request(packet):
    """ Log HTTP request details (IP, host, and timestamp). """
    if packet.haslayer("Raw"):
        data = packet["Raw"].load.decode(errors="ignore")
        if "Host:" in data:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip = packet["IP"].src if packet.haslayer("IP") else "Unknown"

            # Extract visited URL
            host_line = [line for line in data.split("\n") if "Host:" in line]
            if host_line:
                site = host_line[0].split(":")[1].strip()

                with open("../logs/http_logs.txt", "a") as file:
                    file.write(f"{timestamp}, IP: {ip}, Site: {site}\n")
                print(f"🌐 {timestamp} | IP: {ip} → {site}")

if __name__ == "__main__":
    capture_http_requests()
