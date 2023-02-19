#server side code
import os
from socket import *
host = " "
port = 130000
buf = 1024
address = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(address)
print("Waiting to receive messages...")
while True:
    (data, address) =  UDPSock.recv(buf)
    print("received message: " +data)
    if(data == "exit"):
        break

UDPSock.close()
os._exit(0)