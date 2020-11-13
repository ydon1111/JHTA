from random import randint
import pandas as pd
import joblib
import random
import py_source.common.DbConn

def get_locals():
    city1 = list()
    
    with open("static/file/local/locals.csv", "r", encoding="UTF-8") as file:
        for words in file.readlines():
            c1 = words.split(',')[0]
            if c1 not in city1 : city1.append(c1)
        
    return city1

def get_city2(get_city1):
    city1 = list()
    city2 = list()
    
    with open("static/file/local/locals.csv", "r", encoding="UTF-8") as file:
        for words in file.readlines():
            word_list = words.split(',')
            city1.append(word_list[0])
            city2.append(word_list[1].strip())
        
    f_index = city1.index(get_city1)
    l_index = len(city1) - 1 - city1[::-1].index(get_city1) 
        
    return city2[f_index:l_index + 1]
    

def get_dc(city1, city2, sv_list):
    HAPPY_WRITE = [{'content':'행복이란 삶의 최대 관심사다.', 'w': '루스 베네딕트'},
                   {'content':'행복이란 우리가 시간을 들여 열중하는 모든 것이다.', 'w': '알베르 카뮈'},
                   {'content':'행복은 삶의 목적이다.', 'w': '달라이 라마'},
                   {'content':'행복은 축복의 횟수가 아니라 행복을 대하는 우리의 태도일 뿐이다.', 'w': '알렉산더 솔네니친'},
                    {'content':'행복은 사물에 있는 것이 아니라 취햐에 있다.', 'w': '라 로슈푸코'},
                    {'content':'행복은 자기도 모르게 스스로의 힘으로 사랑받고 있다는 확신이다.', 'w': '빅토르 위고'},
                    {'content':'행복은 한순간이며 머물지 않는다. 신이 행복의 돛을 산산이 부숴버리기 때문이다.', 'w': '에우리피데스'},
                    {'content':'행복은 잠깐 나타나서 우리를 한순간 기쁘게 해주는 나비 같다.', 'w': '애나 파블로바'},
                    {'content':'행복은 너무 빨리 날아간다.', 'w': '토머스 그레이'},
                    {'content':'행복은 손으로 물을 잡으려는 것과 같다. -미켈란젤로 안토니오니'},
                    {'content':'행복은 햇살과 같아서 아주 작은 그림자로도 차단된다.', 'w': '중국 격언'},
                    {'content':'행복은 붙잡자마자 사라지는 에우리디케 같다.', 'w': '드니 드 루즈몽'},
                    {'content':'행복은 붙잡지 않는 손에만 내려앉는 천국의 새다.', 'w': '존 베리'},
                    {'content':'행복은 다른 일을 하는 과정에서 얻게 되는 부산물이다.', 'w': '올더 헉슬리'},
                    {'content':'행복은 우연히 온다. 행복을 추구의 대상으로 삼으면 결코 달성할 수 없다.', 'w': '너대니얼 호손'},
                    {'content':'행복은 배움이며 소득이자 열망이다.', 'w': '릴리언 기시'},
                    {'content':'행복은 행복에 있는 것이 아니라 그 성취에 있다.', 'w': '도스토예프스키'},
                    {'content':'행복은 도착지가 아니라 여행 방법이다.', 'w': '마거릿 리 런베크'},
                    {'content':'행복은 한 면에서만 기대해서는 안 된다.', 'w': '지그문트 프로이트'},
                    {'content':'행복은 우리 중 어느 누구도 같은 길로 인도하지 않는다.', 'w': '찰스 칼렙 콜턴'},
                    {'content':'행복은 다양하고 유쾌한 의식 속에 있다.', 'w': '새뮤얼 존슨'},
                    {'content':'행복은 사소한 일에서 곧바로 즐거움을 알아채는 것이다.', 'w': '휴 월폴'},
                    {'content':'행복은 사소한 것에 있다.', 'w': '존 러스킨'},
                    {'content':'행복은 절제된 습관과 소박한 소망에서 비롯된다.', 'w': '제임스 우드'},
                    {'content':'행복은 다른 사람들도 행복해하는 모습을 보는 데 자신을 비치는 것이다.', 'w': '버트런드 러셀'},
                    {'content':'행복은 큰 사랑과 수많은 봉사다.', 'w': '올리브 슈라이더'},
                    {'content':'자신을 위해서만 찾는 행복은 절대로 발견될 수가 없다.', 'w': '토머스 머턴'},
                    {'content':'행복은 바닷가에 홀로 평화로이 남겨져 있는 것이다.', 'w': '루이 페르디낭 셀린'},
                    {'content':'행복은 부도 화려함도 아닌 평온과 일이다.', 'w': '토머스 제퍼슨'},
                    {'content':'행복은 마음이 평온에 있다.', 'w': '키케로'},
                    {'content':'행복은 무엇보다도 순진무구의 평온하고 만족스러운 현실성이다.', 'w': '헨리크 입센'},
                    {'content':'행복은 순진무구다.', 'w': '마르게리트 유르스나르'},
                    {'content':'행복은 명징한 양심이다.', 'w': '에드워드 기번'}
             ]
    
    local_mean = pd.read_csv('static/file/local/total_raw_mean.csv', engine='python') # 행복지수, GNI
    load_happiness_dc = joblib.load('static/file/local/svm_1.pkl') # model load
    
    city2 = city2.strip() # 빈칸제거
    
    city_info = local_mean.loc[(local_mean['city'] == city1) & (local_mean['city2'] == city2)] # 선택 지역의 행복 요소 평균, 지수 정보
    hp2 = float(city_info['hp2'].values[0]) # 지역 행복 역량 지수
    hp3 = float(city_info['hp3'].values[0]) # 지역 평균 삶의 만족도 점수
    h = float(city_info['h_mean'].values[0]) # 건강
    e = float(city_info['e_mean'].values[0]) # 경제
    s = float(city_info['s_mean'].values[0]) # 관계 사회
    ed = float(city_info['ed_mean'].values[0]) # 교육
    sf = float(city_info['sf_mean'].values[0]) # 안전
    l = float(city_info['l_mean'].values[0]) # 여가
    en = float(city_info['en_mean'].values[0]) # 환경
    
    sv_point = sum(sv_list) / 100 # 삶의 만족도 점수
    
    X_res = pd.DataFrame([{'hp3': sv_point, 'hp2': hp2}])
    y_res = load_happiness_dc.predict(X_res)[0]
    
    return {'y_res':y_res, 'sv_point':sv_point, 'hp3':hp3, 'hp2':hp2, 'h':h, 'e':e, 's':s, 'ed':ed, 'sf':sf, 'l':l, 'en':en, 'ws' : HAPPY_WRITE[randint(0, len(HAPPY_WRITE) - 1)]}
