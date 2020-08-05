#클라이언트 사이드
from socket import *
import threading
import time



ip = "192.168.0.68"
port = 5000

def send(sock):
    while True:
        sendData = input(">>>")
        clientSock.send(sendData.encode("utf-8"))

def recive(sock):
    while True:
        recvData = sock.recv(1024)
        print("서버가 보낸 메시지 :" , recvData.decode("utf-8"))

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip,port))

print("접속완료")

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=recive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass