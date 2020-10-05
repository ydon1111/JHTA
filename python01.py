# # Numpy (Numerical Python)
# numpy 배열은 동일한 자료형을 가지는 값들이 격자판 형태로 있는것
# 파이썬이 계산 과학 분야에 이용될때 핵심역할을 하는 라이브러리의 모음

# 빠르고 메모리를 효율적으로 사용하며 백터 산술연산과 세련된 브로드캐스팅 기능을 제공하는 다차원 배열 ndarray
# 반복문을 작성할 필요없이 전체 데이터 배열에 대해 빠른 연산을 제공하는 표준수학함수
# 배열 데이터를 디스크에 쓰거나 읽을 수 있는 도구와 메모리에 올려진 파일을 사용하는 도구

# 선형대수,난수 발생기,푸리에 변환 가능
# c,c++,포트란으로 쓰여진 코드를 통합하는 도구
import math

grades = [1,3,-2,4]
#
# def 함수명(매개변수):
#     처리할문장;
#     처리할문장;
#

def grades_sum(s):
    tot =0
    for i in s:
        tot += i
    return tot

print(grades_sum(grades))

def show_grades(s):
    for i in s:
        print(i, end=', ')

print(show_grades(grades))


def grades_avg(s):
        # tot = 0
        # for i in s:
        #     tot += i
        # return tot/len(s)
        return grades_sum(s)/len(s)


print(grades_avg(grades))


def grades_variance(s):
    tem = 0
    for i in s:
        tem += ((i-grades_avg(s))**2)
    return tem/len(s)
print(grades_variance(grades))


def grades_std(s):
    return math.sqrt(grades_variance(s))

print("평균 : ", grades_avg(grades))
print("분산 : ",grades_variance(grades))
print("표준편차 : ", grades_std(grades))