s = "pPoooyY"
# s = "Pyy"

# def solution(s):
#     counter = {}
#     for i in s:
#         if i not in counter:
#             counter[i.upper()] = 0
#         counter[i.upper()] += 1
    

    

#     return counter
# print(solution(s))




# def solution(s):
#     p = s.lower().split("p")
#     y = s.lower().split("y")
#     pcount = []
#     for i in p:
#         if i == '':
#             i.append(pcount)
#     ycount = []
#     for r in y:
#         if r == '':
#             r.append(ycount)
    
#     if pcount in ycount:
#         print(pcount)
# print(solution(s))


def solution(s):
    l = s.lower()
    r = s.lower()
    k = l.count('p')
    y = r.count('y')
    if k == y:
        return True
    else:
        return False


        # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )