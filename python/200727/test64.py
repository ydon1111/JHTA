import os
#운영체제에서 제공되는 여러 기능을 파이썬에서 수행할수 있게 해주는 모듈: os

# print(dir(os))

# 현재 작업 디렉토리

# print(os.getcwd())

# #현재 작업디렉토리에 있는 파일과 디렉토리 목록 검색

# print(os.listdir('200727'))
# print(os.listdir('../..')) # . 현재 디렉토리 : E:\dev\python_workspace
#                            # .. 부모디렉토리 : 

# print(os.listdir("E:\\dev\\python_workspace"))

#현재 작업 디렉토리에 있는 모든 파일을 출력 
#반복문을 사용하여 한개씩 출력 
#확장자가 .zip 파일만 선택 
for i in os.listdir('c:/'):
    if i.find('.zip') != -1:
        print(i)
    if i.endswith('.zip'):    #??
        print(i)









