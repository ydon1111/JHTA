'''
정수 내림차순으로 배치하기
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	    return
118372	873211
'''

n = 118372



# def solution(n):
#     r = list(str(n))
#     r.sort()
#     return r
   
# print(solution(n))
   
l = list(str(n))
l.sort()
l.reverse()
an = ''
for i in l:
    an+=str(i)
ans = int(an)
return ans 


1
2
3
4
5
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))




2
3
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)));