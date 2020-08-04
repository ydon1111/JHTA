

#with open("파일명",파일모드) as 파일객체:
# 코드 

# with open("./200727/msg.txt",'w')as file:
#     file.write('오늘은 여기까지...\n')

with open("./200727/msg.txt",'r')as file:  
    data = file.read().count('인식')
    print(data)

    # for i in file.read().split():
    #     if i.find("인식") != -1:
    #         print(i)








