# 제어문
# 조건 분기문
# 주어진 조건 발생하면 다른 문장이 실행되게 처리 
'''
if 조건:
    처리할문장
    처리할문장
elif 조건:
    처리할문장2
    처리할문장2
    처리할문장2
else: 
    처리할문장3
    처리할문장3
'''

# score = int(input('당신의 성적을 입력하세요 :'))


# if score>=90:
#     print('당신의 성적은 ', score , "입니다. A학점")
#     print('축하합니다. 짝짝짝!!!')
# elif score>=80:
#     print('당신의 성적은 ', score , "입니다. B학점")
# elif score>=70:
#     print('당신의 성적은 ', score , "입니다. C학점")
# elif score>=60:
#     print('당신의 성적은 ', score , "입니다. D학점")
# else:
#     print('당신의 성적은 ', score , "입니다. F학점")

# 1부터 20까지 값을 출력
#1. 1, 2, 3, 4, 5, 6, 7, 8, 9, ---20
#2. 홀수만 출력 (if)


for i in range(1,21):
  if i%2 == 1: #홀수번째 구하기 2로 나눠서 나머지가 1인것들 
      print(i)


# 구구단 5단 출력 


for dan in range(5,6):
    for i in range(1,10):
        if i%2 ==1:
            print(str(dan)+" * "+str(i)+"="+str(dan*i))
        else:
            print(str(dan)+" * "+str(i)+"="+str('****'))



# 5 * 1 = 5
# 5 * 2 = ****
# 5 * 3 = 15
# 5 * 4 = ****