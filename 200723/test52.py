# map : built-in 함수 : list 나 dictionary 와 같은 iterable 한 데이터를 인자로 받아 
# list 안에 개별 item 을 함수의 인자로 전달하여 결과를 list형태로 주는 함수 


def func1(x):
    return x*2 
#간단한 로직 

m = [10,20,30,40]
n=[]
for i in range(len(m)):
   n.append(func1(m[i]))
print(n) # [20,40,60,80]


print(list(map(func1,m)))

t = {1:100,2:200,3:300}

print(list(map(func1,t)))
print(list(map(func1,[ t[i] for i in t])))

a = [1,2,3,4,5,6,7,8,9,10]

# 3의 배수만 출력
print([str(i) for i in a if i%3 ==0])

#makeString(x)
# 'x' 

def makeString(x):
    if x%3 == 0:
        return str(x)
    else:
        x
        return x





print(list(map(lambda x : str(x) if x%3==0 else x ,a)))


# #소수?
# def primeNumber(x):
#     # 실수로리턴
#     # 아니면 자기자신
#     if x == int(x):
#         x = float(x)
    
#람다식으로 출력
#filter : 조건에 일치하는 값만 추출할때 사용하는 함수 

def test2(x):
    if x>0:
        return x
    else:
        return None


n = [-3,-2,-1,0,1,2,3]

print(list(filter(test2,n)))

print(list(filter(lambda x : x>0 ,n)))   

#60 이상
score = [80,70,53,90,70,80,49,99]

print(list(filter(lambda x : x>60 ,score)))  

#70점이상 90점 사이 

print(list(filter(lambda x : x>=70 and x<=90 ,score))) 

file_names = ['movie1.jpg','movie.png','rabbit.png','bg.png','test.txt','test2.py']

#png 파일의 확장자만 검사해서 파일의 이름
#['movie2.png','rabbit.png','bg.png']
print('-----------------------------------------------')

print(list(filter(lambda x : x.find('.png')>0,file_names))) 

def png_Finder(x):
    if x.find('.png') != -1:
        return x 
    else:
        return None



print(list(filter(png_Finder,file_names)))
print(list(filter(lambda x : x.find('.png') != -1,file_names)))




