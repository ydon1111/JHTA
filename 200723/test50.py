

def do_test(*k):
    r=0
    for i in k:
        r += i
    print(r)
    return r

#리턴값이 있는 함수는 
x = do_test(300,100,200,300)


def do_test1 (**kwargs):           # keyword 와 values 값을 같이 가져옴
    for key,val in kwargs.items():
        print('key :', key, 'value :', val)


do_test1(name="홍길동",age=20)
