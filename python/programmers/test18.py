'''
약수의 합
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
입출력 예
n	return
12	28
5	6
입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
'''

n = 12 
re = 1,2,3,4,6,12
def solution(n):
    i=0
    r=[1,]
    if n ==0:
        return 0
    while n > i+1:
        i += 1 
        if n%i == 0:
            k = n//i 
            # print(k)
            # print(i)
            r.append(k)
        else:
            continue
        
    return sum(r)

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])



print(solution(0))