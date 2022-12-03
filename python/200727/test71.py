with open("./200727/msg3.txt",'r') as file:
    data = file.readlines()
    print(data)

lines = ['안녕하세요\n','오늘은 금요일\n','이면 좋겠어요\n']

with open("./200727/msg3.txt",'w') as file:
    file.writelines(lines)


