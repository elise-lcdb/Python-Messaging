import os
from socket import *

host = "10.1.6.253"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Enter your message to send or type 'exit': ")
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)