import os
from socket import *

host = "207.23.174.138"
port = 130000

address = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter a message or type exit to exit: ")
    UDPSock.sendto(data,address)
    if data == "exit":
        break

UDPSock.close()
os._exit(0)