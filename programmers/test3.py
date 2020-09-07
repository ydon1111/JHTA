
'''participant 에 있는 것을 빼옴
completion에 있는것과 비교
없으면 없는 것을 빼서 출력 
동명이인이면 따로 출력 '''



participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# print(set(participant))
# print(participant - completion)
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]


# def solution(participant,completion):
#     for i in participant:
#         for r in completion:
#             print(i,r)
            
#             # if i != r:
#             #     print(i)



# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range (len(completion)):
#         if completion[i] != participant[i]:
#             return participant[i]
#             return participant[len(participant)-1]
       



# def solution(participant, completion):
#   participant.sort()
#   completion.sort()
#   for i in completion:
#         participant.remove(i)
    
#     answer = participant[0]          
#     return answer


# print(solution(participant,completion))
       
def solution(participant, completion):      
    participant.sort()
    completion.sort()
    for index in range(len(completion)):
            if completion[index] != participant[index]:
                # 동명이인 중에 완주 못한 사람 체크
                return participant[index]
        # 동명이인이고 완주를 하지 못했으나 이름 상 제일 뒤에 있는 사람인 경우 체크
        # 예시) 정렬된 후의 변수가 participant['a', 'b', 'b', 'z', 'z'] / completion['a', 'b', 'b', 'z'] 인 경우
    return participant[-1]


import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer




def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
