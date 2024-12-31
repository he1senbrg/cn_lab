from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print('The server is ready to receive\n')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()

    if message and modifiedMessage:
        print(f"Received '{message.decode()}' from {clientAddress}")
        print(f"Sending '{modifiedMessage}' to {clientAddress}\n")

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)