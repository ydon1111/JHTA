# PS E:\dev\python_workspace> pip install apscheduler
from apscheduler.schedulers.background import BackgroundScheduler 
from apscheduler.jobstores.base import JobLookupError 
import time 

def wther(): 
    print("wther", "| [time] " , str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
    print("날씨 크롤링")
    print("----------------------------------------------")
    
def rcd(): 
    print("rcd", "| [time] " , str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
    print("추천 크롤링")
    print("----------------------------------------------")

def line():
    print("----------------------------------------------")

sched = BackgroundScheduler() 
sched.start() 

# interval - 매 3조마다 실행 
# sched.add_job(job, 'interval', seconds=3, id="test_2") 
# interval - 매 시간 10분 마다 실행 
sched.add_job(wther, 'cron', minute="10", second='0', id="wther") 
sched.add_job(rcd, 'cron', minute="10", second='0', id="rcd")
sched.add_job(line, 'interval', seconds=600, id="line")

while True:
    pass
    
    
    