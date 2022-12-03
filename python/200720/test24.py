msg = input("영어를 입력하세요 : ")

# 이 글자를 소문자로 변환 시키자 
# ord(문자) ==> ascii code
# chr(숫자) ==> 문자
#hello
# 1.각 글자의 ASCII 코드 값을 구한다.
# 2. 대문자범위 : 65~90 이라면 이것을 대문자로 바꾼다.
# 3. 소문자 :97~122  대소문자는 ASCII 코드 32 만큼 차이남
# 4. 변환된 값을 출력 

print(len(msg))        #5
for i in range(len(msg)):
        # print(msg[i])
        code = ord(msg[i])
        if code >=65 and code <= 90:
            print(chr(code+32),end="")
        elif code >=97 and code <= 122:
            print(chr(code-32),end="")


