#현재 작업중인 디렉토리경로를 얻어오기
import os 
print(os.getcwd())

# 파일 입출력 

# open('파일명','모드')

file = open('./200727/hello.txt','r')
print(file)
print(file.read(),type(file.read()))
file.close()


print('--------------------------------')

file2 = open("./200727/hello2.txt","w")
print(file2)
file2.write("금요일 같은 월요일..월요병")

help(file2.write)

file.close()