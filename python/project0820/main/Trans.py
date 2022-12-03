


# 주간 날씨 박스
NorwayList = ['Cludy', 'Fair', 'Heavy rain', 'Heavy rain showers' ,'Light rain' , 'Light rain showers', 'Partly cloudy' ,'Rain' ,'Rain showers','Clear sky','Fog']

#NowayList는 DB에서불러오는 값으로 변경
korTran = ""
if NorwayList[1] == 'Cludy' or NorwayList[1] == 'Fog':
    korTran = "흐림"
elif NorwayList[1] == 'Heavy rain showers' or NorwayList[1] == 'Light rain showers' or NorwayList[1] ==  'Rain showers':
    korTran =  "소나기"
elif NorwayList[1] == 'Fair':
    korTran = "구름조금"
elif NorwayList[1] == 'Light rain':
    korTran = "흐리고 비"
elif NorwayList[1] == 'Heavy rain' or NorwayList[1] == 'Rain' or NorwayList[1] == 'Rain':
    korTran = "비"
elif NorwayList[1] == 'Partly cloudy':
    korTran = "구름많음"
elif NorwayList[1] == 'Clear sky':
    korTran = "맑음"
elif NorwayList[1] == 'Light rain and thunder':
    korTran = "뇌우"
print(korTran)

#아이콘 파일명 딕셔너리에서 불러오기 
koreaDic= {'맑음':"w1",'구름조금':"w3",'구름많음':"w5",'흐림':"w7",'소나기':"w8",'비':"w9",'흐리고 비':"w10",'구름많고 비':"w10",'뇌우':"w17"}
print(koreaDic['맑음'])