#server side code
import os
from socket import *
import translator

host = ""
port = 13000
buf = 2048

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind((host, port))

print("Waiting to receive messages...")

while True:
    message, clientAddresss =  UDPSock.recvfrom(buf)
    
    # Translate the message from English to Mountain
    modifiedMessage = translator.englishToMoutain(message.decode())
    
    print("Message received: " + modifiedMessage)
    
    # Translate the message from Mountain to English
    translatedMessage = translator.mountainToEnglish(modifiedMessage)
    
    UDPSock.sendto(translatedMessage.encode(), clientAddresss)
    
    if message.decode() == "exit":
        break

UDPSock.close()
os._exit(0)
