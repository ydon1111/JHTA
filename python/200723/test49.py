
def setEncrytion(msg):
    v =""
    for i in range(len(msg)):
        #msg의 문자열에서 한글자씩 ASCII 구한다.
        code = ord(msg[i])
        #코드 값에 +3
        code += 3 
        if code >= 91 and code <= 93:
            code -= 26
        elif code >= 123 and code <=125:
            code -= 26
        print(chr(code))
        v +=chr(code)
    return v

def getDecode(msg):
    k =""
    for i in range(len(msg)):
        code = ord(msg[i])
        code -= 3 
        if code >= 91 and code <= 93:
            code += 26
        elif code >= 123 and code <=125:
            code += 26
        print(chr(code))
        k +=chr(code)
    return k



data = 'hello'
x = setEncrytion(data)
y = getDecode(x)
print(x)
print(y)

import random 
com = []
cnt = 0 
while len(com) <= 2:
    rnd = random.randint(0,9)
    if rnd in com:
        continue
    else:
        com.append(rnd)
print(com)
while True:
    cnt +=1
    userData = int(input('3자리숫자를 입력하세요'))
    user = []
    user[0] = userData//100
    user[1] = userData%100//10
    user[2] = userData%10
    print(user)

    strike =0
    ball =0

    for i in range(3):
        if com[i] == user[i]:
            strike += 1
        else:
            for j in range(3):
                if com[i] == user[j]:
                    ball +=1
    print(strike,"s",ball,"b")

    if strike ==3:
        print("축하합니다.",cnt,"번만에 성공")
        break