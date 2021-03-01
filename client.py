import sys
import socket
import struct

ETH_P_ALL=3
s=socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind(("eth0", 0))
r=s.recvfrom(2000)
# sys.stdout.write("<%s>\n"%repr(r))

packet = r[0]

# take first 20 characters for the ip header
ip_header = packet[0:20]

# now unpack them :)
iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

version_ihl = iph[0]
version = version_ihl >> 4
ihl = version_ihl & 0xF

iph_length = ihl * 4

eth_length = 14
eth_header = packet[:eth_length]
eth = struct.unpack('!6s6sH', eth_header)
eth_protocol = socket.ntohs(eth[2])
t = iph_length + eth_length
tcp_header = packet[t:t+20]

tcph = struct.unpack('!HHLLBBHHH' , tcp_header)
source_port = tcph[0]
dest_port = tcph[1]
sequence = tcph[2]
acknowledgement = tcph[3]
doff_reserved = tcph[4]
tcph_length = doff_reserved >> 4
h_size = eth_length + iph_length + tcph_length * 4
data_size = len(packet) - h_size

data = packet[h_size:]