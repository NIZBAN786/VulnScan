import scapy.all as scapy

# scapy.ls(scapy.IP)

# scapy.ls(scapy.TCP)

# scapy.ls(scapy.UDP)

# scapy.ls(scapy.ICMP)

# scapy.ls(scapy.Ether)

# scapy.ls(scapy.ARP)

def packet_callback(packet):
    packet.show()
    scapy.sniff(prn=packet_callback, count=10)

