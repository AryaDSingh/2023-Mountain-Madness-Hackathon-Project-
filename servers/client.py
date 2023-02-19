import os
from socket import *

host = "207.23.174.138"
port = 13000

address = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    # make this equal to the translated message
    message = input("Enter a message or type exit to exit: ")
    UDPSock.sendto(message.encode(),address)
    modifiedMessage, clientAddress = UDPSock.recvfrom(2048)
    print(modifiedMessage.decode())
    if message == "exit":
        break

UDPSock.close()
os._exit(0)