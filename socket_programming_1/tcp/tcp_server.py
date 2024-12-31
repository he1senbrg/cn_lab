from socket import *

serverPort = 13000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive\n')

while True:
    connectionSocket, addr = serverSocket.accept()
    
    message = connectionSocket.recv(2048)
    modifiedMessage = message.decode().upper()

    if message and modifiedMessage:
        print(f"Received '{message.decode()}' from {addr}")
        print(f"Sending '{modifiedMessage}' to {addr}\n")

    connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()