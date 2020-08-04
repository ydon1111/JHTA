import random

#랜덤 모듈 가져옴 
#0,1값을 랜덤으로 가져옴  
#만약 값이 0이면 20%인상
#아니면 그대로 

#만약 값이 0이면 20%인하
#아니면 그대로 


def raise_rnd_salary(sale):
    n = random.randint(0,1)                    
    if n == 0:
        print("강화성공")
        return int(sale*1.2)
    else:
        return sale

def reduece_rnd_salary(sale):
    n = random.randint(0,1)                    
    if n == 0:
        print("강화실패")
        return int(sale*0.8)
    else:
        return sale

if __name__ =="__main__":             
    print(reduece_rnd_salary(2000))
    print(raise_rnd_salary(2000))