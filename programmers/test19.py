'''
시저 암호
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
입출력 예
s	       n	result
AB	        1	BC
z	        1	a
a B z	    4	e F d

'''

s = "a b z"
n = 1
# print(ord("b"))
# print(ord(" "))
def solution(s,n):
    re = ""
    # t = 0
    for i in list(s):
        if ord(i) != ord(" "):
            t = ord(i) + n
            if 97<=ord(i)<=122:
                if 122<t:
                    t = t - 122 + 96
                # print(t,"소문자")
                    re += chr(t)
                else:
                    re+= chr(t)
            elif 65 <= ord(i)<=90:
                if 90<t :
                    t = t - 90 + 64
                # print(t,"대문자")
                    re += chr(t)
                else:
                    re+=chr(t)
        else:
            re += " "  
    return re
            
            
            


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
#         if 122<t:
#             t = t - 122 + 96
#             # print(t,"소문자")
#             re += chr(t)
#         elif 90<t :
#             t = t - 90 + 64
#             # print(t,"대문자")
#             re += chr(t)
#         else:
#             re += chr(t)   
#     else:
#         re += " "
# return re

print(solution("qrstuvwxyz QRSTUVWXYZ   ABCDEFG abcdefg",9))

# print(ord("q"))
# print(ord("p"))


# 97 ~ 122 소문자

# 65 ~ 90 대문 



# msg = input("영어를 입력하세요 : ")

# # 이 글자를 소문자로 변환 시키자 
# # ord(문자) ==> ascii code
# # chr(숫자) ==> 문자
# #hello
# # 1.각 글자의 ASCII 코드 값을 구한다.
# # 2. 대문자범위 : 65~90 이라면 이것을 대문자로 바꾼다.
# # 3. 소문자 :97~122  대소문자는 ASCII 코드 32 만큼 차이남
# # 4. 변환된 값을 출력 


# print(len(msg))        #5
# for i in range(len(msg)):
#         # print(msg[i])
#         code = ord(msg[i])
#         if code >=65 and code <= 90:
#             print(chr(code+32),end="")
#         elif code >=97 and code <= 122:
#             print(chr(code-32),end="")

