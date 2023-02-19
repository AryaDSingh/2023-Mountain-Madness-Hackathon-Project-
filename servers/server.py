#server side code
import os
from socket import *
host = " "
port = 13000
buf = 2048
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(('',port))
print("Waiting to receive messages...")
while True:
    message, clientAddresss =  UDPSock.recvfrom(buf)
    #translate the message back into english
    modifiedMessage = message.decode()
    print("Message received: "+modifiedMessage)
    UDPSock.sendto(modifiedMessage.encode(), clientAddresss)
    if message == "exit":
        break

UDPSock.close()
os._exit(0)