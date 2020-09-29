library(datasets)
library(lattice)
str(airquality)
#1973 뉴욕의 대기에 대한 질을 측정한 데이터셋
#153개의 관측치 6개의 변수
#Ozone , Solar.r(태양광),Wind,Temp,측정월 (5~9),day 1~31 

head(airquality)
xyplot(Ozone~ Wind|factor(Month),data = airquality,layout=c(5,1))

data(quakes)
str(quakes)
#1964년 태평양에서 발생 지진위치 

#위도 경도 
tplot<-xyplot(lat~long, data=quakes,pch="x")
tplot
#그래프에 제목 추가 
tplot2<-update(tplot,main = "1964년 태평양에서 발생한 지진위치")
tplot2

#eqal.count() : 지정된 범위 대상 영역구분과 카운팅
#형식 : equal.count(data,number,overlap)
#지진의 깊이를 3영역으로 구분하여 카운팅

depthgroup<-equal.count(quakes$depth,number=3,overlap=0)
depthgroup

xyplot(lat~long|depthgroup,data=quakes,main="태평양 피지섬 주변의 지진발생위치",ylab=
         "Latitude",xlab="longitue",pch="@",col="red")

#cloud() : 3차원(위도,경도,깊이): 산점도 그래프 

cloud(depth~lat*long,data=quakes,zlim = rev(range(quakes$depth)),xlab = "경도",ylab = "위도",zlab="깊이")
 

#두집단 평균차이 검정

data <- read.csv(file = "two_sample.csv",header = T )
data

head(data)
summary(data)
# score: NA's : 73 
# 두집단 subset 작성 (데이터 정제, 전처리)
result <- subset(data, !is.na(score),c(method,score))
result
length(result$score)

# 교육방법 별로 분리

a <- subset(result,method==1)
b <- subset(result,method==2)
a 
b

length(a$score)
length(b$score)
# 귀무가설 : 두 집단간 분포의 차이가 없다
# 귀무가설 : 두 집단간 분포의 차이가 있다

#분포 모양 검정 : 두 집단의 분포 모양 일치여부 검정 

var.test(a$score,b$score)
# F = 1.2158, num df = 108, denom df = 117, p-value = 0.3002 
# 귀무가설 채택
# 정규분포 여부 확인

# 동질성 분포 : t.test() 귀무가설 채택시 사용 
# 비동질성 분포 : wilcox.test() 귀무가설 기각시 사용



# 가설검정 - 두 집단 평균 차이 검정 
# 귀무가설 : 두집단간 평균차이 없다
# 대립가설 : 두집단간 평균차이 있다
t.test(a$score,b$score)
t.test(a$score,b$score,alternative = "two.sided",conf.level = 0.95)

# 단측검정
t.test(a$score,b$score,alternative = "greater",conf.level = 0.95)

t.test(a$score,b$score,alternative = "less",conf.level = 0.95)
# 낮은쪽에서 차이가 있다 a가 b 보다 크지 않다 


# 세 집단 간 비율 차이 검정

data2 <- read.csv("three_sample.csv",header =T)
data2
str(data2)

# 1 score NA 제외
result2 <- subset(data2, !is.na(score),c(method,survey,score))
method <- data2$method
survey <- data2$survey
method
survey

# 
# 교육방법      인원    만족
# 1.이론교육    50
# 2.실습교육
# 3.혼합교육

x <- c(1,NA,3,4,NA,5)
x
table(x)
table(x, useNA="ifany")
table(x, useNA="always")

table(method, useNA="no")
table(method, survey)

#세 집단 만족도 비율차이검정

#h0 : 세 집단간 만족율의 차이가 없다
#h1 : 세 집단간 만족율의 차이가 있다 

#prop.test(그룹별빈도,그룹수)
prop.test(c(34,37,39),c(50,50,50))

# 세집단간 교육방법에 따른 집단간 만족율에 차이가 없다고 할 수 있다. 

# 세집단의 평균차이 검정

# 귀무가설 : 교육방법에 따른 세 집단간의 시험의 평균 성적 차이가 없다
# 대립가설 : 교육방법에 따른 세 집단간의 시험의 평균 성적 차이가 있다 

# score <- NA 제외 

df <- read.csv("three_sample.csv",header = T )
df

df <- subset(df,!is.na(score),c(method,score))
head(df)
summary(df)
plot(df)

# 14 이상 되는 값은 outlier 제거 

df <- subset(df,score<=14)
df

df$method2[df$method==1] <- "이론교육"
df$method2[df$method==2] <- "실습교육"
df$method2[df$method==3] <- "혼합교육"
df

head(df$method2)
table(df$method2)

#정구성 검정
#셋 이상의 모집단들이 동일한 분산을 갖는지에 대한 검정
# bartlett.test(종속변수~독립변수)
# 귀무가설 : 세집단간의 분포의 모양 차이가 없다
# 대립가설 : 세집단간의 분포의 모양 차이가 있다

bartlett.test(score~method2,data=df)
# 
# 
# 동일한 집단
# anova
# 동일하지 않은 경우
# kruskal.test()
# 
# aov(종속변수~독립변수)

aov(score~method2,data=df)
result <- aov(score~method2,data=df)

names(result)
summary(result)

# 9.39e-14 *** < 0.05 : 귀무가설 기각

# 집단간 평균차이가 존재한다라고 할수 있다.

TukeyHSD(result)
# 
# 이론교육-실습교육 -2.612903
# 이론교육과 실습교육의 차이가 가장 크다 
# 
# iris

# 귀무가설 : 품종별 sepal.width 평균차이가 존재하지 않는다. 
# 대립가설 : 품종별 sepal.width 평균차이가 존재하지 한다
data <- iris
data(data)
str(data)

data$Species2[data$Species=="setosa"] <- 1
data$Species2[data$Species=="versicolor"] <- 2
data$Species2[data$Species=="virginica"] <- 3

plot(data)
data
bartlett.test(Sepal.Width~Species2,data=data)
result <- aov(Sepal.Width~Species2,data=data)

summary(result)

TukeyHSD(result)


result <- read.csv("product.csv",header = T)
head(result)
str(result)

# 기술통계량 
# ????
# 각 변수별 표준편차 
# ????
# 상관계수 

summary(result)
sd(result$제품_친밀도)
sd(result$제품_적절성)
sd(result$제품_만족도)

cor(result$제품_친밀도,result$제품_적절성)
cor(result$제품_친밀도,result$제품_만족도, method = "pearson")

cor(result,method = "pearson")

install.packages("corrgram")
library(corrgram)

corrgram(result)
corrgram(result,upper.panel = panel.conf)

#차트에 곡선과 별표 표시 
install.packages("performanceAnalutics")
library(PerformanceAnalytics)

#상관관계 , p , 정규분포 시각화 
chart.Correlation(result,histogram = ,pcj="+")

#iris 데이터셋에서 각 독립변수끼리으 상관성 여부를 판단한 후에 이것을 시각화

data <- iris
data(data)
str(data)

data$Species2[data$Species=="setosa"] <- 1
data$Species2[data$Species=="versicolor"] <- 2
data$Species2[data$Species=="virginica"] <- 3

data$Species
data2 <- data[-5]

cor(data2,method = "pearson")
chart.Correlation(data2,histogram = ,pcj="+")


#--------------------------------------------------------

# 예측 : 회귀분석
# regression analysis

# 단순회귀분석 
# 독립변수와 종속변수가 1개인 경우

# 제품 적절성은 제품의 만족에 양의 영향을 미친다 

# 귀무가설 : 제품 적절성은 제품의 만족에 양의 영향을 미치치 않는다
# 대립가설 : 제품 적절성은 제품의 만족에 양의 영향을 미친다 

# 독립변수 : 제품 적절성 
# 종속변수 : 제품 만족도 

# 선형회귀 모델 
# lm(y~x, data)

str(result)
x <- result$제품_적절성
y <- result$제품_만족도

result.lm <- lm(formula = y~x , data = result)

summary(result.lm)

plot(x,y,ylim = c(1,10),xlim = c(1,10))

abline(result,im,col="blue")



abline(a=0.77886,b=0.73928,col="red")

# y=0.77886+0.73828X

#-----------------------------------------------------------------------------


# 영화진흥위원회 사이트에서 박스오피스 영화 정보를 가져오기
# 네이버에서 영화제목으로 별점 가져오기
# df
# 영화제목 별점, 매출액, 스크린수, 장르, 별점
# 상관관계
# 시각화
library(rvest)
library(httr)
library(xlsx)
library(dplyr)
url<-"https://movie.naver.com/movie/search/result.nhn?query="
movie<-read.csv("movie2.csv", header = T, sep = ",")
movie
movie<-head(movie, 10)
txt<-NULL
rating<-NULL
genre<-NULL
for (i in movie$영화명) {
  movie_name<-paste0(url,URLencode(i))
  txt<-read_html(movie_name)
  rating[i]<-txt%>%html_node("#old_content > ul.search_list_1 > li:nth-child(1) > dl > dd.point > em.num")%>%html_text()
  genre[i]<-txt%>%html_node("#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dd:nth-child(3) > a:nth-child(1)")%>%html_text()
}


rating
movie

df<-cbind(movie[2],rating,movie[4],movie[8],genre)
colnames(df)<-c("영화제목", "별점", "매출액", "상영횟수", "장르")

df
# 상관관계
library(stringr)
# df$별점<-str_replace_all(format(df$별점),",","")
df$매출액<-str_replace_all(format(df$매출액),",","")
df$상영횟수<-str_replace_all(format(df$상영횟수),",","")


df$별점<-as.numeric(format(df$별점))
df$매출액<-as.numeric(format(df$매출액))
df$상영횟수<-as.numeric(format(df$상영횟수))

cor(df[2:4])

# 시각화
library(corrgram)
corrgram(df[2:4], upper.panel=panel.conf)
library(PerformanceAnalytics)
chart.Correlation(df[2:4], pch="+")

