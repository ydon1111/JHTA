
'''
1. 
세계 최초의 암호화   : setEncryption(문자열) 

	1. 사용자로부터 단어를 입력받는다.    ex) HELLO 
		  
	2. 3번째 뒤에 글자를 출력한다.         ex) ~~~~~ 

	예) A ==> D
	    C ==> F
	    B ==> E 

	getDecode(~~~~~)

	HELLO 
'''
# def setEncryption():
#     msg = input("글자 입력하세요 :")      
#     res = ""
#     for i in range(len(msg)):
#         code = ord(msg[i])
#         if code >=65 and code <= 87:
#             res += chr(code+3)
#         elif code >=88 and code <=90: 
#             res += chr(code-23)
#         elif code >=97 and code <= 119:
#             res += chr(code+3)
#         elif code >=120 and code <= 123:
#             res += chr(code-23)
#     return res 

# def getDecode(data):
#     msg = data
#     res = ""
#     for j in range(len(msg)):
#         code = ord(msg[j])
#         if code >=65 and code <= 87:
#             res += chr(code-3)
#         elif code >=88 and code <=90: 
#             res +=chr(code+23)
#         elif code >=97 and code <= 119:
#             res +=chr(code-3)
#         elif code >=120 and code <= 123:
#             res +=chr(code+23)   
#     return res
    
# enc = setEncryption()
# dec = getDecode(enc)

# print(enc,dec)


'''
2.

score 리스트에 국어 , 영어 , 수학 점수가 들어있다.
총점과 평균을 계산해서 리스트에 담은 후 모든
학생의 국어, 영어, 수학, 총점, 평균을 출력하시오
참고) 리스트에는 국어, 영어 수학 점수만 들어있다.

score = [
	[80,80,80,0,0],
	[60,50,80,0,0],
	[50,90,90,0,0],
	[40,50,60,0,0],
	[90,90,95,0,0],
	[85,95,100,0,0] ]
'''

# score = [
# 	[80,80,80,0,0],
# 	[60,50,80,0,0],
# 	[50,90,90,0,0],
# 	[40,50,60,0,0],
# 	[90,90,95,0,0],
# 	[85,95,100,0,0] ]

# for i in score:
#     g = i[0]
#     e = i[1]
#     m = i[2] 
#     tot = g+e+m 
#     avg = tot/3
#     i[3] = tot
#     i[4] = avg
#     print(g,e,m,tot,avg)
# print(score)



# for i in range(6):
#     for j in range(len(score[i])):
#         print(score[i][j])







'''
3.

야구 게임 (BaseBall)
3자리의 숫자 랜덤 생성 : 397
자리와 숫자가 모두 동일 하면 strike
자리는 다르지만 다른 자리에 숫자가 존재하면 볼

입력:307
출력 : 2S

입력:379
출력: 1S2B

입력:397
출력: 정답 축하합니다. 3회만에 성공하셨습니다.

[알고리즘]
1. 컴퓨터가 세자리숫자를 생성한다.
2. 사용자로부터 3자리숫자를 입력받는다.
3. 판별한다.
	(자리와 숫자가 일치하면 :strke
	자리는다르지만 숫자가일치하면 : ball)
4. 출력한다.
5. 3strike이면 종료한다.
6. 아니면 2번으로 돌아가서 반복한다.
'''

# import random
# k =[]
# i = 0
# while i <3:
#     num = random.randint(1,9)
#     if num in k:
#         continue
#     else:    
#         k.append(num)
#         i += 1
# print(k)
		
# c = 0
# while True:
#     u =list(input("숫자 3개 입력 :" ))
#     s = 0
#     b = 0 
#     for i in range(3):
#         if str(k[i]) == u[i]:
#             s = s+1
#         elif str(k[i]) in u:
#             b = b+1
#     c = c+1
#     print("스트라이크",s,"볼",b)
#     if s == 3: 
#         break
# print("축하합니다.",c,"회만에 성공")





'''
4.

	printGuGuDan(2, 6) ; 

	// 2단 부터 6단까지 출력하는 함수를 구현하세요 
'''

# def printGuGuDan(n1,n2):
#     for j in range(n1,n2+1):
#         print(j,"단")
#         for i in range(1,10): 
#             print( j,"*",i,"=" ,j * i ) 
        
    
    
# printGuGuDan(2,6)
        
 