from scapy.all import Ether, IP, UDP, sendp

# Configura las direcciones MAC e IP
src_mac = "28:80:23:a9:b4:7c"
dst_mac = "00:15:4d:13:5C:AB"
src_ip = "192.168.60.241"
dst_ip = "10.2.0.1"

# Configura los puertos de origen y destino
src_port = 12345    
dst_port = 6890

# Crea el contenido del mensaje UDP
payload = "Este es el mensaje que quiero enviar"

# Construye el paquete Ethernet con las direcciones MAC
eth = Ether(src=src_mac, dst=dst_mac)

# Construye el paquete IP con las direcciones IP
ip = IP(src=src_ip, dst=dst_ip)

# Construye el segmento UDP con los puertos y el mensaje
udp = UDP(sport=src_port, dport=dst_port)

# Construye el paquete final
packet = eth / ip / udp / payload

# Envía el paquete
sendp(packet, iface="vf0_1")
sendp(packet, iface="vf0_1")
print("Paquete enviado.")
