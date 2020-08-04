

#CPU 
#Thread : 하나의 프로세스 내에서 진행되는 하나의 싱행 단위를 의미 
#MultiThread

#프로세서 : 메모장, 워드 , 카톡 
#멀티 쓰레드 : 카톡 : 채팅 , 파일 전송

#파이썬에서 멀티 쓰레드 구현 방법
#1. 쓰레드가 실행 할 함수 혹은 메서드를 작성하는 방식
#2. threading.Thread 로부터 파생된 파생클래스를 작성하여 사용하는 방식


import threading

def run(who):
    for i in range(1,101):
        print(str(i) +"미터 달리는중",who)

# run("번개")
# run("천둥")


#멀티 쓰레드 처리 
t1 = threading.Thread(target=run,args=("번개",))
t2 = threading.Thread(target=run,args=("천둥",))


#start() : 쓰레드를 동작시킨다.
t1.start()
t2.start()

print("main Tread end ..............")