#web Crawling 
#여러 사이트를 정기적으로 여러 사이트를 정기적으로 돌며 정보를 추출하는 기술 
#==> DB 

#web Scraping
#웹사이트 특정 정보를 추출하는 기술 


#HTML ,CSS, Javascript

import requests

res = requests.get('https://www.google.com/')
print('응답코드 :',res.status_code)


# 200: 정상 (HTTP:status)
# 404: 페이지를 찾을 수 없음: url 오류
# url (Uniform Resource Location)
# 500: 서버 사이드 로직 에러 

# if res.status_code == requests.codes.ok:
#     print(len(res.text)) 


res.raise_for_status() #에라가 있으면 에러 메시지를 출력하고 바로 종료 

# print("aaaaaa")
# print(res.txt)

with open("googole.html","w",encoding="utf-8") as f:
    f.write(res.text)