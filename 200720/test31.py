# while True:
#     value = int(input("숫자를 입력:"))
#     #5의 배수인가요?
#     if value%5 == 0 :
#         continue                                 #조건이 맞으면 다시 처음으로 돌아감
#     print(str(value)+"는 5의 배수가 아닙니다.")
# print('이제그만.....')


#1부터 100까지 수중 3의 배수 5개만 출력 
# tot = 0
# for i in range(1,100):
#     if i%3 == 0:
#         tot+=1
#         print(i)
#         if tot == 6:
#             break
        
#이문장이 더 효율적임
tot = 0
for i in range(1,100):
    if i%3 == 0 and tot <5:
        tot+=1
        print(i)


        


     
