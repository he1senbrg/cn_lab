from socket import *

serverName = '192.168.207.237'
serverPort =  12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('\nInput lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(f"Modified message from server: {modifiedMessage.decode()}\n")

clientSocket.close()