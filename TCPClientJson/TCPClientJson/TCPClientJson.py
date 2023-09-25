from socket import *
import json

serverName = '127.0.0.1'
serverPort = 12000
clientSocket  = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    print('Pick Either: Random, Add or Subtract:')
    case = input()
    
    print('Write first number:')
    firstNumber = input()
    
    print('Write second number')
    secondNumber = input()
    
    protocolOptions = {
        "case" : case,
        "firstNumber" : int(firstNumber),
        "secondNumber" : int(secondNumber)
        }
    jsonText = json.dumps(protocolOptions)
    clientSocket.send(jsonText.encode())
    recievedMessage = clientSocket.recv(1024).decode()
    print(json.loads(recievedMessage))