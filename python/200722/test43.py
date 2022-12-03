
#function : 함수 
#반복되는 코드를 줄여주기 위해 특정 코드에 이름을 부여해 놓은것 
#내장함수 
#def 함수명(매개변수,매개변수,매개변수):
#         실행문장
#         실행문장
#         return 결과값
# print('11111111111111')
# def double(num1):
#     print('22222222222')
#     return num1 * 2
# print('333333333333')

# y = double(10)   #argument , 인수
# print(y)

# k = double(20)
# print(k)

#불러서 실행 : 호출


#로또번호 생성기

# 1. 랜덤하게 1부터 45 까지 생성
# 2. 로또 리스테에 담는다
# 3. 중복된 값이 있으면 다시 뽑는다.
# 4. 6자리가 모두 완성되면  
# 5. 정렬한다.
# 6. 출력한다.

def getLotto(x):
    for i in range(x):
        lotto = []
        import random 
        i =0
        while i<6:
            num = random.randint(1,45)
            if num in lotto:
                continue                   #진행 안하고 처음으로 돌아감 continue
            else:
                lotto.append(num)
                i+=1
            lotto.sort()
            
        print(lotto)

getLotto(5)

