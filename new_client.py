import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect(("192.168.1.201", 8000))
sock.recvfrom(2000)

try:

    client = sock.getsockname()[0]
except socket.error:
    client = "Unknown IP"
finally:
    del sock
print(client)
