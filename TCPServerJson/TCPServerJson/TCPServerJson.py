from socket import *
import threading
import json
import random

def handleClient(connectionSocket, addr):
    while True:
        inputRecieved = connectionSocket.recv(1024).decode()
        jsonText = json.loads(inputRecieved)
        case = jsonText["case"]
        firstNumber = int(jsonText["firstNumber"])
        secondNumber = int(jsonText["secondNumber"])
        sendResult = ""
        if case != "Random" and case != "Add" and case != "Subtract":
            sendResult = case + " unknown case"
        if case == "Random":
            if firstNumber > secondNumber:
                sendResult = "First number is greater than second number"
            elif firstNumber == secondNumber:
                sendResult = "First and second number is equal"
            elif secondNumber > firstNumber:
                sendResult = json.dumps(random.randint(firstNumber,secondNumber))
        if case == "Add":
            sendResult = firstNumber + secondNumber
        if case == "Subtract":
            sendResult = firstNumber - secondNumber
        jsonResult = json.dumps(sendResult)
        connectionSocket.send(jsonResult.encode())

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient,args=(connectionSocket, addr)).start()