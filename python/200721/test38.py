''' 1부터 100사이의 정수를 랜덤하게 생성
    사용자로부터 숫자 한개를 입력
    두수가 일치하면 일치합니다. 메세지 출력
    일치하지 않으면 일치하지 않습니다 메세지 출력 
    일치 하지 않으면 사용자가 입력한 수보다 큰값인지 작은값인지 출력
    다시 2번으로 이동 
'''
import random

num = random.randint(1,100)
print(num)
while True:
    guess = int(input("1부터 100사이의 정수를 입력하세요 : ")) 
    if num == guess:
        print('두수가 일치합니다.')
        break
    else:
        if num >= guess:
            print('더큰수로 입력')
        else:
            print('더작은수로 입력')
    print('두수가 일치하지 않습니다.')
