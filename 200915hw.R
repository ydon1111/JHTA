1. 다음과 같은 벡터를 칼럼으로 갖는 데이터프레임을 생성하시오.
name <-c("둘리","콩순이", "뽀로로","뽀","나나")
age <-c(55,45,45,53,15) #연령
gender <-c(1,2,1,1,1) #1:남자, 2: 여자
job <-c("연예인","주부","군인","직장인","학생")
sat <-c(3,4,2,5,5) # 만족도
grade <- c("C","C","A","D","A")
total <-c(44.4,28.5,43.5,NA,27.1) #총구매금액(NA:결측치)

# <조건1> 위 7개 벡터를 user이름으로 데이터 프레임 생성


user <- data.frame(NAME=name , AGE = age, GENDER = gender , JOB = job , SAT = sat, GRADE=grade 
                   ,TOTAL = total)

user


2. Data를 대상으로 apply()를 적용하여 행/열 방향으로 조건에 맞게 통계량을 구하시오.

kor <- c(90,85,90)
eng <- c(70,85,75)
mat <- c(86,92,88)    

# 조건1) 3개의 과목점수를 이용하여 데이터프레임(Data)을 생성한다. 
score <- data.frame(KOR=kor,ENG= eng, MAT=mat)
score
# 조건2) 행/열 방향으로 max()함수를 적용하여 최댓값 구하기
apply(score,1,max)
apply(score,2,max)
# 조건3) 행/열 방향으로 mean()함수를 적용하여 평균 구하기(소숫점 2자리 까지 표현)
#  힌트 : round(data, 자릿수)
round(apply(score,1,mean),2)
round(apply(score,2,mean),2)

# 조건3) 행 단위 분산과 표준편차 구하기  

apply(score,2,var)
apply(score,2,sd)

3 다음의 Data2 객체를 대상으로 정규표현식을 적용하여 문자열을 처리하시오
Data2 <- c("2017-02-05 수입3000원","2017-02-06 수입4500원","2017-02-07 수입2500원")
library(stringr)

# 조건1) 일짜별 수입을 다음과 같이 출력하시오. 
#        출력 결과) "3000원" "4500원" "2500원" 
Data2
Data3 <- unlist(str_extract_all(Data2,"[0-9]{4}[가-힣]{1}"))
Data3
# 조건2) 위 벡터에서 연속하여 2개 이상 나오는 모든 숫자를 제거하시오.  
#        출력 결과) "-- 수입원" "-- 수입원" "-- 수입원"  
Data4 <- str_replace_all(Data2,"[0-9]","")
Data4
# 조건3) 위 벡터에서 -를 /로 치환하시오.
#        출력 결과) "2017/02/05 수입3000원" "2017/02/06 수입4500원" "2017/02/07 수입2500원"  

Data5 <- str_replace_all(Data2,"-","/")
Data5
# 조건4) 모든 원소를 쉼표(,)에 의해서 하나의 문자열로 합치시오. 
Data6 <- paste(Data2, collapse = ",")
Data6
# 힌트) paste(데이터셋, collapse="구분자")함수 이용
#        출력 결과) "2017-02-05 수입3000원,2017-02-06 수입4500원,2017-02-07 수입2500원"