
# keyword = "오늘은 비가 언제 까지 올까요?".split()

# print(keyword, type(keyword))

# #각 단어가 몇글자인지 알아내기

# print({len(word) for word in keyword},type({len(word) for word in keyword}))  #set 특징 중복이 사람짐

# #3자 초과만 선택해서 
# print({len(word) for word in keyword if len(word) >3})

#dictionary Comperhension

countrys = {"한국":"서울","일본":"도쿄","중국":"북경","UAE":"아부다비"}

#key 값만 출력

capital = {country : capital for country,capital in countrys.items()}   #items ?????

print(capital)

