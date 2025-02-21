from scapy.all import sniff
import datetime

def packet_callback(packet):
    if packet.haslayer("DNS"):
        domain = packet["DNS"].qd.qname.decode("utf-8")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("../logs/dns_logs.txt", "a") as file:
            file.write(f"{timestamp}, Domain: {domain}\n")
        print(f"🌐 {timestamp} | {domain}")

def start_dns_sniffing():
    """ Start packet sniffing for DNS requests """
    print("📡 Monitoring DNS Requests...")
    sniff(filter="udp port 53", prn=packet_callback, store=0)

if __name__ == "__main__":
    start_dns_sniffing()
