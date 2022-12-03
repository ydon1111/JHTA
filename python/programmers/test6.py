'''
x만큼 간격이 있는 n개의 숫자
문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.
입출력 예
x	n	answer
2	5	[2,4,6,8,10]
4	3	[4,8,12]
-4	2	[-4, -8]
'''
# k = -4
# j = 2

#실패 
# z = []
# for i in range(k-1,j+1):
#     t =  k * i 
#     print(t)
#     z.append(t)
# print(z)


# def solution(x, n):
#     j=1
#     answer = []
#     while j <= n:
#         t =  x * j
#         answer.append(t)
#         j+=1
#     return answer




# def number_generator(x, n):
#     # 함수를 완성하세요
#     return [i * x + x for i in range(n)]
# print(number_generator(2, 5))    



# list(range(x, x*n+1, x))


print([i*5 + 4 for i in range(5)])