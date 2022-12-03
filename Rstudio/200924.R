x<-rnorm(1000000,0,10)
mean(x)

hist(x)

#적분 


density(x) #밀도 계산 

plot(density(x))
#확률 밀도 함수
#주어진 변량이 정해진 구간안에 존재 할 확률을 나타내는 함수 

#실험에서 나타난 결과를 실수로 표현한 변수 x 확률변수 

#동전 두개를 던졌을때 앞면의 갯수 
#단일 집단 비율 차이 검정 

data <-read.csv("one_sample.csv",header = T)
data
str(data)
x <- data$survey
x
#결측치 
length(x)
table(x)


install.packages("prettyR")
install.packages("Hmisc")
library(prettyR)
library(Hmisc)


freq(x)
# 만족율 기준 비율 검정
# 귀무가설 : 올해의 고객만족율과 작년(80%)과 차이가 없다.
# 대립가설(연구가설) : 올해의 고객만족율과 작년과 차이가 있다. 

binom.test(c(136,14),p=0.8) # 80%
# number of successes = 136, number of trials = 150, p-value = 0.0006735
# p-value = 0.0006735  < 0.05
# 귀무가설을 기각 
# 올해의 고객만족율과 작년(80%)과 차이가 없다고 할 수 없다.
# 불만족율 

# binom.test() 
# 명목척도의 비율을 바탕으로 binom.test() 이항 분포의 
# 양측검정을 통해서 검정통계량을 구한 후 이를 이용해서 가설을 검정 

# 귀무가설 : 올해의 고객 불만족율이 작년(20)과 차이가 없다.
# 대립가설 : 올해의 고객 불만족율이 작년(20)과 차이가 있다.

# binom.test(x,n,p,alternative = )
# x 성공의 수 , 실패의 수
# n 시행의 수 
# p 확률 
# alternative = : 양측검정 , 단측검정
# "two.sided" ,"greater","less"


binom.test(x= 14,n =150,p=0.2,alternative = "two.sided")
# number of successes = 14, number of trials = 150, 
# p-value = 0.0006735 < 0.05 
# 귀무가설을 기각
# 올해의 고객 불만족율이 작년(20)과 차이가 있다고 할 수 있다.

# 귀무가설 : 올해의 고객 불만족율은 작년(20)보다 크지 않다
# 대립가설 : 올해의 고객 불만족율은 작년(20)보다 크다

binom.test(x=14,n=150,p=0.2,alternative = "greater",conf.level = 0.95)
# number of successes = 14, number of trials = 150, 
# p-value = 0.9999 > 0.05 
# 귀무가설을 채택
# 올해의 고객 불만족율은 작년(20)과 크지 않다 할 수 있다.



#----------------------------------------------------------
# 벡터 v : 1 or 0 의 값을 100개 생성
# 출력
# 1: 동전의 앞면은 0은 동전의 뒷면이라고 하자.
# 동전의 앞면 비율이 45%인지 검정하시오
# 아니라면 큰지? 작은지? 검정하세요
#----------------------------------------------------------

# rbinom(100,1,0.5)

set.seed(999999)
v <- sample(x=c(1:2),100,replace = T)
v


freq(v)
# binom.test(x=50,n=100,p=0.45)
# number of successes = 50, number of trials = 100, 
# p-value = 0.317 >0.025 
# 채택 

binom.test(x=57,n=100,p=0.45)
binom.test(x=57,n=100,p=0.45,alternative = "greater")



binom.test(x=57,n=100,p=0.45,alternative = "less")



data <- read.csv("two_sample.csv",header =T)
data
str(data)
dim(data)
table(data$survey)
table(data$method)

#두 집단의 만족도 비율 차이 검정
# 
# 귀무가설 : 두 집단의 만족도 비율의 차이가 없다
# 대립가설 : 두 집단의 만족도 비율의 차이가 있다

# 모집단의 모비율 차이에 대한 검정 : prop.test()

# 흡연자와 비흡연자 폐암 발병률의 차이 
# A학교 B학교 야구부 선수들의 평균 타율 

x<-data$method
x
y<-data$survey
y
table(x,y)

prop.test(c(110,135),c(150,150))

# X-squared = 12.824, df = 1, 
# p-value = 0.0003422 <0.025
#귀무가설 기각
#대깁가설 채택 

#귀무가설 방법1 만족도 비율 <= 방법2 만족비율 
#대립가설 방법1 만족도 비율 > 방법2 만족비율

prop.test(c(110,135),c(150,150), alternative = "greater",conf.level = 0.95)

# 
# X-squared = 12.824, df = 1, 
# p-value = 0.9998 > 0.05 
# 귀무가설 채택 

#대응 두 집단 평균차이 검정
# 조건 a집단 독립적 b 집단
# 비교대상 독립성유지
# 대응:표본이 짝을 이룬다

data <-read.csv("paired_sample.csv",header=T)
data

dim(data)
str(data)
table(data$after)
table(data$before)

summary(data$before)
summary(data$after)

!is.na(data$after)
result<- subset(data,!is.na(after),c(before,after))
result

head(result,5)

after <- result$after
before <- result$before

mean(after)
mean(before)


#동질성 검정
#귀무가설 : 두집단의 분포모양의 차이가 없다
#대립가설 : 두집단의 분포모양의 차이가 있다. 


var.test(before, after,pared =T)
 
# F = 1.0718, num df = 95, denom df = 95, 
# p-value = 0.7361

#귀무가설 : 다이어트약 복용 전후에 차이가 없다 
#대립가설 : 다이어트약 복용 전후에 차이가 있다 

t.test(before, after , paired = T)

# t = -13.642, df = 95, 
# p-value < 2.2e-16
# 귀무가설 기각
 
# 귀무가설 : 다이어트 약 복용 전 >= 후
# 대립가설 : 다이어트 약 복용 전 < 후 

# 방향성을 갖는 단측가설 검증
t.test(before,after,paired = T, alternative = "less", conf.level = 0.95)
# data:  before and after
# t = -13.642, df = 95, p-value < 2.2e-16
# 귀무가설 기각 
# before을 기준으로 비교 : before가 after 보다 적다.

# t.test() 를 실시하기 위해서 , 등분산성, 정규성을 만족해야 t.test()
# 만족해야 t.test()

# 두집단 데이터 

a <- c (175,168,168,190,156,181,182,175,174,179)
b <- c (185,169,173,188,186,175,174,179,180,173)


df <- data.frame(a,b)
df
summary(df)
# 두집단의 평균차 검정

#동질성 검사 

#귀무가설 : 두집단의 분산이 차이가 없다.
#대립가설 : 두집단의 분산이 차이가 있다. 
var.test(a,b)
#귀무가설 채택 
#두집단의 평균차 검정 
 
# studetn's T test 
# 1. 연속형수치
# 2. 두 집단은 서로 독립적
# 3. 정규성을 가져야 한다.
# 4. 추정된 분산은 동일해야한다

# product.csv 파일 읽어오기기

result <- read.csv(file="product.csv",header = T)
result

table(result)
summary(result$제품_만족도)

var(result$제품_친밀도)
var(result$제품_적절성)
var(result$제품_만족도)

sd(result$제품_친밀도)
sd(result$제품_적절성)
sd(result$제품_만족도)

#각 변수의 표준편차

#각 변수들의 산점도 
plot(result$제품_친밀도,result$제품_만족도,xlim=c(0,8),ylim=c(0,10))
plot(result$제품_적절성,result$제품_만족도,xlim=c(0,8),ylim=c(0,10))

# 제품의 친밀도,만족도 상관관계

cor(result$제품_친밀도,result$제품_만족도)
cor(result$제품_친밀도,result$제품_적절성)


cor(result, method = "pearson")

# 방향성이 있는 
install.packages("corrgram")
library(corrgram)

corrgram(result)
corrgram(result,upper.panel = panel.conf)
corrgram(result,lower.panel = panel.conf)


install.packages("PerformanceAnalytics")
library(PerformanceAnalytics)

#상관성, p(값), 정규분포 시각화 
chart.Correlation(result,histogram=,pch="+")

#--------------------------------------------------------------------

install.packages("ggiraphExtra")
library(ggiraphExtra)
#미국 주별 범죄 데이터 준비하기
# R에 내장된 USArests 데이터 :1973년 미국 주별 강력범죄율 정도
data(USArrests)
str(USArrests)
head(USArrests)
library(tibble)

crime <- rownames_to_column(USArrests,var="state")
crime$state <- tolower(crime$state)
str(crime)
#단계 구분도를 만들려면 지역별 위도, 경도 정보가 있는 지도 데이터가 필요하다.
#R에 내장된 maps 패키지에 미국 주별 위경도를 나타내는 state 데이터가 들어있다.

#ggplot2 패키지의 map_data()를 이용해 이 데이터를 프레임으로 불러오쟈
library(ggplot2)
library(plotly)
library(maps)
library(mapproj)
library(stringi)
install.packages("stringi")
install.packages("plotly")
install.packages("maps")
install.packages("mapproj")

states_map <- map_data("state")
str(states_map)
states_map
len(states_map
    )

ggChoropleth(data=crime , aes(fill =Murder,map_id=state), map=states_map,interactive = T)

#----------------------------------------------------------
# write.csv(korpop1,file ="korpop1.csv",quote = F,fileEncoding = "UTF-8")

install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014")
library(kormaps2014)
library(dplyr)
korpop1
str(korpop1)
str(changeCode(korpop1))

korpop1 <- changeCode(korpop1)

korpop1 <- rename(korpop1,pop=총인구_명, name=행정구역별_읍면동)
korpop1
korpop1$name <- iconv(korpop1$name, "UTF-8","CP949")
korpop1$pop <- as.numeric(korpop1$pop)
korpop1
ggChoropleth(data=korpop1,aes(fill=pop,map_id=code,tooltip=name),map=kormap1,interactive=T)
#----------------------------------
install.packages("lattice")

library(lattice)

install.packages("mlmRev")
library(mlmRev)

# mlmRev 패키지에서 제공되는 데이터셋으로 1997년 영국 2280개 학교 31022학생들 대상으로 A레벨(대학시험)화학점수를 기록한 
# 데이터셋

str(Chem97)
dim(Chem97)
#lea(Local Education Authority): 지방교육청 
# school 학교 ID
# student 학생 ID
# score 화학점수 (범위 : 0,2,4,6,8,10)
# gender성별 (범위 : M,F)
# age 18.5 (범위 -6,5)
# gcsescore : GCSE 개인평균성적(범위 : 0~8 사이 실수)
# gcsecnt

head(Chem97,30)
# 
# histogram : GCSESCORE 변수 대상 백분율 적용 
# 히스토그램 : histogram(~x축,dataframe)

histogram(~gcsescore,data=Chem97)

# histogram(~축|조건,dataframe)
histogram(~gcsescore|factor(score),data=Chem97)
#score 
# 밀도그래프프
densityplot(~gcsescore|factor(score),data=Chem97,groups = gender,plot.points=T,auto.key=T)

#iris 데이터셋에서 각 독립변수끼리의 상관성 여부 판단
#시각화 

iris
irisdata <- cor(iris[-5], method = "pearson")

result2<- iris[-5] 
corrgram(result2,upper.panel=panel.conf)

# histogram(~Sepal.Length|Sepal.Width,data = iris)



#영화진흥위원회 사이트에서 2019년도 정보를 가져오기
#네이버에서 영화제목으로 별점 가져오기
#df 
#영화제목 별점,매출액,스크린수 장르 별점 
#상관관계
#시각화 


library(rvest)


box <- read.csv(file = "kobis1.csv",header = T,sep = ",",)
box <- head(box,10)
box
names(box)

url <-"https://movie.naver.com/movie/search/result.nhn?&section=all&ie=utf8&query="
keyword <- 
  


txt1<-read_html(url)
txt1
navermovie <- txt1 %>% html_node("#content > div.article > div:nth-child(1) > div.lst_wrap > ul") %>% html_text()
navermovie


