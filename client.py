import sys
import socket
import struct

ETH_P_ALL=3
s=socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind(("eth0", 0))
r=s.recvfrom(2000)
# sys.stdout.write("<%s>\n"%repr(r))


# packet string from tuple
packet = r[0]

# take first 20 characters for the ip header
ip_header = packet[0:20]

# now unpack them :)
iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

version_ihl = iph[0]
version = version_ihl >> 4
ihl = version_ihl & 0xF

iph_length = ihl * 4

ttl = iph[5]
protocol = iph[6]
s_addr = socket.inet_ntoa(iph[8]);
d_addr = socket.inet_ntoa(iph[9]);

print('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))

tcp_header = packet[iph_length:iph_length + 20]

# now unpack them :)
tcph = struct.unpack('!HHLLBBHHH', tcp_header)

source_port = tcph[0]
dest_port = tcph[1]
sequence = tcph[2]
acknowledgement = tcph[3]
doff_reserved = tcph[4]
tcph_length = doff_reserved >> 4

print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))

h_size = iph_length + tcph_length * 4
data_size = len(packet) - h_size

# get data from the packet
data = packet[h_size:]

print('Data : ' + data)