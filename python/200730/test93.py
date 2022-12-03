class Car:
    def __init__(self):
        print("초기화 함수")
    def __str__(self):
        #문자열화 해 반환
        return "str method 가 호출됨"
    def __del__(self):
        print("소멸자 호출 : 더이상 안써요 폐차 ")
    #매직함수: 가장 일반적인 용도 : 오퍼레이터 오버로딩용 가장 많으 사용

    # + : def __add__
    # - : def __sub__
    # * : def __mul__
    # / : def __trudiv__
    # //: def __floordiv__
    # % : def __mod__
    #** : def __pow__
    # < : def __lt__
    # > : def __gt__
    # >=: def __ge__


c2 = Car()

print(str(c2))


del c2 


