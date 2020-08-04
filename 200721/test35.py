
#가위 바위 보 
#가위 바위 보 라는 글짜를 담은 리스트를 만듬
#0,1,2 중 한계를 리턴하는 함수를 사용
#출력


#사용자 값 받기
import random   
print("1. 가위 2. 바위 3. 보")
userInput = int(input("가위 바위 보 중 선택하세요 : "))
userInput -= 1


#랜덤하게 뽑기
game = ["가위","바위","보"]
idx = random.randint(0,2)
print(idx,game[idx])

#승부판정
#사용자의 입력값 , 컴푸터의 랜덤값의 차를 비교
# print("사용자입력값" ,userInput,game[userInput])
# print("컴퓨터랜덤값" ,idx ,game[idx])
# print("차이값", userInput-idx)


dif = userInput-idx
#차이값 0  이라면  비김
if dif ==0:
    print("비김")
elif dif ==1 or dif ==-2:
    print("사용자승")
elif dif == -1 or dif ==2:
    print("컴퓨터승")
#1 이거나 -2 이면  사용자승

#-1 이거나 2 이면  컴퓨터승

