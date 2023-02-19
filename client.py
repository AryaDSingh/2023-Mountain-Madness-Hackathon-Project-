#client side code
import os
from socket import *
import translator

host = "192.168.100.121"
port = 13000

address = (host, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("Enter a message or type exit to exit: ")
    
    # Translate the message from English to Mountain
    translatedMessage = translator.englishToMoutain(message)
    
    UDPSock.sendto(translatedMessage.encode(), address)
    
    modifiedMessage, serverAddress = UDPSock.recvfrom(2048)
    
    # Translate the message from Mountain to English
    modifiedMessage = translator.mountainToEnglish(modifiedMessage.decode())
    
    print(modifiedMessage)
    
    if message == "exit":
        break

UDPSock.close()
os._exit(0)
