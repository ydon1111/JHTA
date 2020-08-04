#임포트 하는 방법 3가지
# 1.import 모듈명

# import random
# import math

# 2. from 모듈명 import 함수명 

from random import randint
# from deabak import randint  다른 모듈에 동일한 함수가 있을 경우 충돌날 우려 있음

n = randint(100,200)
print(n)

print(dir())

# 3. from 모듈명 import *

# from random import *
# print(dir())

import math