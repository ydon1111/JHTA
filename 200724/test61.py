

def make2(fn):
    return lambda : '곤니찌와' + fn()    
    # def test2():
    #     return '곤니찌와' +fn()
    # return test2
   

def make1(fn):
    return lambda : '니하오' + fn()           #fn()  --> 함수만 실행 
#   def 이름없음():
#       return "니하오" + fn()
#   return 이름없음


def hello():
    return "한라봉"

t = make1(hello)
t2 =make2(t)

print(t())
print(t2())



#데코레이터(decorator) ; 장식하는 도구 
@make2 
@make1                                     # @  -- > 함수안에 함수 넣기 
def hello2():
    return '소망이'


hi = hello2
print(hi())