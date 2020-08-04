#csv 파일

# a , b , c  = input("숫자 3개를 콤마로 구분해서 입력하세요: ").split(",")

# print("a :", a , "b :" , b , "c :" , c )


print(100,200,300, sep=", ") #sep을 통해서 문자사이에 원하는 기호 삽입

print("Hello","python","world", sep=" ") #sep을 통해서 문자사이에 원하는 기호 삽입

print(100,200,300, sep =" \n") #sep을 통해서 문자사이에 원하는 기호 삽입 , \n 은 enter 

# 
# \n == enter 
# \t == tap 

print("아\n 날씨가 \n 좋다. \t \t \t 놀러 가야 ")

print("오늘은" ,end="\t") # 오늘은 \n
print("수요일" ,end="\t")
print("내일은" ,end="\t ,\t")
print("목요일" )

# 사용자가 입력한 3개의 숫자중 가장 큰수를 출력 


# year , month , day , hour , minute , second 변수를 선언하고 
# 값을 대입한후에
# 아래와 같은 출력을 얻도록 코드를 작성 

# 오늘은 2020/7/15 18:00:00 입니다.

# 2020/7/15

year = '2020'
month = '7'
day = '15'
hour = '18' 
minute = '00'
second = '00'


print('오늘은' + year , month , day , sep="/",end =" ") # 각 문장을 변수 선언후에 문장사이에 / 넣고 끝 부분 합침 
print(hour , minute , second + '입니다.', sep= ":"  )   # 각 문장을 변수 선언후에 문장사이에 :





