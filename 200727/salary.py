#연관된 함수들의 모음 : 모듈
author = "홍길동"

def raise_sal(sal):
    '''
        급여를 10%인상
    '''
    return int(sal*1.1)

def reduce_sal(sal):
    return int(sal*0.8)
        # sal - (sal*0.2) = 1(sal) - 0.2(sal) = 0.8(sal)


#test Code 
if __name__ == "__main__":
    print(__name__)    #__m^.^m__
    print(raise_sal(3000))
    print(reduce_sal(1000))
    print("잘나오나? :",author)



