#클라이언트 사이드


from socket import *

ip = "192.168.0.35"
port = 5000



def send(sock):
    sendData = input(">>>")
    clientSock.send(sendData.encode("utf-8"))

def recive(sock):
    recvData = sock.recv(1024)
    print("서버가 보낸 메시지 :" , recvData.decode("utf-8"))

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip,port))

print("접속완료")



while True:
    recive(clientSock)
    send(clientSock)