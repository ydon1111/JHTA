
def solution(s):
    if len(str(s)) >=1 and len(str(s)) <=100: 
        if len(s)%2 ==0:
            answer = s[round((len(s)/2)-1)] +s[round((len(s)/2))]
            return answer 
        else:
            answer = s[int(len(s)/2)]
            return answer


# print(len("abc"))
# print((len("abc")-1)//2)
# print(len("abc")//2+1)


# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print((len('abcde')-1)//2)
print(len('abcde')//2+1)

print(string_middle("abcde"))
