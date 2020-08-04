import time

# help(time)

# help(time.time)
print(time.time())

print(time.ctime(),type(time.ctime()))

r = time.ctime().split()

print(r[4])  #print(r[-1])

#지금 시간을 1초에 한번씩 출력 


# while True:
#     time.sleep(1) #1초 잠들어라 
#     print(time.ctime())

print(dir(time))