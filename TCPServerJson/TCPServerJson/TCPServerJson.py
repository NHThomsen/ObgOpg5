from socket import *
import threading

def handleClient(connectionSocket, addr):
    print('hello world')

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient,args=(connectionSocket, addr)).start()