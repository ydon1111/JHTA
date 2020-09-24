'''소수 찾기
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
'''

# 1 부터 10까지 의 숫자를 뽑음

# 각 숫자의 약수를 구함 
# 약수리스트에 2개있으면 answer에 어팬딩
# 아니면 패스 


def solution(n):
    answer = []
    for r in range(2,n+1):
        t = [r]
        for i in range(1,r+1):
            if r%i == 0:
                t.append(i)
        if len(t) == 3:
            a = t[0]
            answer.append(a)
        # print(t)
    return len(answer)  


solution(10)