import time

def saveLog(savedir,money,balance,mode):       
    if mode:
        type = '출금'
    else:
        type = '입금'
    with open(savedir,'a',encoding='utf-8') as file:
        file.write(time.ctime()+'/' + type + str(money) +'/' + '잔액: ' + str(balance)+"\n")
       


