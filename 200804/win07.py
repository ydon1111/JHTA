
from threading import Thread

class MThread(Thread):
    def __init__(self,who):
        super().__init__()
        self.who = who

    def run(self):
        for i in range(1,100):
            print(str(i)+"미터 달리는중",self.who)

h1 = MThread("천둥이")
h2 = MThread("각설탕")

h1.start()
h2.start()

