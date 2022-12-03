#0-9 사이의 정수를 랜덤하게 생성
#예외란? 프로그램 실행중 발생한 예상치 못한 오류 : 가벼운 오류
#예외를 처리해 줄 수 있다 .

#casebycase 

#try:
#   문장1
#   문장2
# except ????:
#   예외처리문장1
#   예외처리문장2

class EvenError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg




import random as r
try:
    n = int(input("숫자를 입력하세요"))
    # 사용자가 입력한 값이 짝수이면 실행안함
    if n%2 ==0:
        raise EvenError("짝수만 입력하세요.")
    
    for i in range(10):
        a = r.randint(0,9)
        print(n/a)

except EvenError as ee:
    print(ee)
    print("짝수는 계산안함")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
except ValueError:
    print("정수만 입력하세요")
finally:
    print("이 부분은 예외가 있던 없던 항상 실행됩니다.")
