from socket import*
import random

serverSock = socket(AF_INET, SOCK_STREAM)   #서버 접속
# 65535 == > 8000-9000  port 개발용 
serverSock.bind(('',5000)) # 5000번 포트를 사용
print("사용자의 접속을 대기합니다.")
serverSock.listen(1) #연결을 기다림 (수신중 .. )
connectionSock, addr = serverSock.accept()   #서버접속 승인
print(str(addr)+"연결 성공!!! ")

data = connectionSock.recv(1024)    #데이터를 받는데 1024문자로 제한
msg = data.decode("utf-8")          #utf-8 문자열로 받음
# print(msg)

#리스트에 10개에 문자열 담음
#랜덤하게 하나씩 뽑아서 
#클라이언트에 전송
lis = ['a','b','c','d','e','f','g','h','i','j']
msg = random.choice(lis)  #랜덤리스트 중에서 하나뽑음
print(msg)    

connectionSock.send(msg.encode("utf-8"))    #클라이언트에 보냄
print("서버 메시지 전송 완리")

