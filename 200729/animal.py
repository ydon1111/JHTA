class Animal:

    #공통되는것은 밖으로 빼야함 .  init 안에 있으면 읽어오지 못함

    def __init__(self,foots):
        print("초기화함수")
        self.eyes = 2
        self.mouth = 1
        self.ears = 2 
        self.foots = foots
        
    def eating(self,eat):
        print(eat,"을 먹어요")

    def sleeping(self):
        print("쿨쿨 자요")
    