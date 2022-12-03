#쥐띠
#태어난 연도를 입력하면 어떤띠인지를 출력

#자축인묘진사오미신유술해
#쥐소호토용뱀말양원닭개돼
#4,5,6,7,8,9,10,11,0,1,2,3
#태어난 년도를 4자리로 입력: 2020
#당신은 쥐띠 입니다.

year = int(input("태어난 연도를 입력하세요 :"))

# if year%12 == 4:
#     print(year, "당신은 쥐띠입니다.")
# elif year%12 == 5:
#     print(year, "당신은 소띠입니다.")
# elif year%12 == 6:
#     print(year, "당신은 호랑이띠입니다.")
# elif year%12 == 7:
#     print(year, "당신은 토끼띠입니다.")
# elif year%12 == 8:
#     print(year, "당신은 용띠입니다.")
# elif year%12 == 9:
#     print(year, "당신은 뱀띠입니다.")
# elif year%12 == 10:
#     print(year, "당신은 말띠입니다.")
# elif year%12 == 11:
#     print(year, "당신은 양띠입니다.")
# elif year%12 == 0:
#     print(year, "당신은 원숭이띠입니다.")
# elif year%12 == 1:
#     print(year, "당신은 닭띠입니다.")
# elif year%12 == 2:
#     print(year, "당신은 개띠입니다.")
# elif year%12 == 3:
#     print(year, "당신은 돼지띠입니다.")


ddi =["원숭이띠","닭띠","개띠","돼지띠","쥐띠","소띠","호랑이띠","토끼띠","용띠","뱀띠","말띠","양띠"]   #리스트에 담음
year %= 12                                         #12로 나눈 나머지를 통해서 리스트에서 인덱스 번호로 뽑음
print(ddi[year])


# year %= 12

