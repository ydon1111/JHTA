# 클라이언트 사이드

from socket import *

clientSock = socket(AF_INET,SOCK_STREAM)
#서버랑 연결해줘
clientSock.connect(('192.168.0.35',5000))  #127.0.0.1 예외적인 아이피 , 루프백 어드레스 
clientSock.send("Yahoooooooo~".encode("utf-8"))            #서버에보냄

data = clientSock.recv(1024)                          #서버가 보낸거 받음
print("서버가 보낸데이터: "+data.decode("utf-8"))      #출력 받은거 utf-8로 받음
print("연결성공!!")

