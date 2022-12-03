arr1 = [[1,2],[2,3]]	
arr2 = [[3,4],[5,6]]

re = [[4,6],[7,9]]

# print(len(arr1))
# print(arr1[0][0] + arr2[0][0])
# print(arr1[0][1] + arr2[0][1])
def solution(arr1,arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for r in range(len(arr1[i])):
            answer[i].append(arr1[i][r]+arr2[i][r])
    return answer

# # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def sumMatrix(A,B):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
#     return answer

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))


import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))



def sumMatrix(A,B):
    answer = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [3,4]], [[3,4],[5,6]]))