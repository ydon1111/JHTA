install.packages("animation")
library(animation)

ani.options(interval=1)
v<- c("안","녕","하","세","요")
v

# text(0.5,0.5,"내용",cex=크기,col="색상")
for (i in c(1:5)){
  plot.new()
  size = 11-i
   rect(0,0,1,1,col="black")
  text(0.5,0.5,v[i],cex=size,col=rgb(1,1,0))
  ani.pause()
}
#-----------------------------------------------------
ani.options(interval=1) # 1초 간격으로
for (i in c(1:10)){
  y<-runif(5,0,1)
  y
  barplot(y,ylime=c(0,1),col=rainbow(5))
  ani.pause()
}
# warnings()

#-------------------------------------------------------

# 1/10 씩 10번에 걸쳐 바차트 완성 

y<- runif(5,0,1)
y
y2<-rep(0,5)
y2

raiseY <- y/10
raiseY



for (i in c(1:10)){
ani.options(interval=(10-i)*0.02)
  y2<-y2+raiseY
  barplot(y2,ylim=c(0,1),col=rainbow(5))
  ani.pause()
}


# 1부터 100 사이의 값을 랜덤하게 10개 
#barchar를 작성
#1/100 나눠서 점점 증가하는 애니메이션 효과

y<-round(runif(10,0,100),0)
y

y2<- rep(0,10)
y2

raiseY<- y/10
raiseY 

for (i in c(1:10)){
  ani.options(interval=(10-i)*0.02)
  y2<-y2+raiseY
  barplot(y2,ylim=c(0,100),col=rainbow(5))
  ani.pause()
}


#-------------------------------------

install.packages("ggplot2")
library(ggplot2)

update.packages()



#레이어 구조
#3층 설정 축,범위,색,표식
#2층 그래프추가(점,막대. .. )
#1층 배경

#mpg

#x축 배기량 , y축 고속도로 연비 산점돔
data(mpg)
plot(mpg$displ,mpg$hwy)

#1층
ggplot(data=mpg,aes(x=displ,y=hwy))
#2층 레이어
#산점도 그리는 함수 : geom_point()
ggplot(data=mpg,aes(x=displ,y=hwy))+geom_point()
#3층 레이어
ggplot(data=mpg,aes(x=displ,y=hwy))+geom_point()+xlim(3,6)


#막대 그래프 
# mpg 데이터에서 drv(구동방식)별 평균hwy(고속도로 연비)막대 그래프 그리기기
# 구동방식별 평균 고속도로 연비비
library(dplyr)
df_mpg<- mpg %>% group_by(drv) %>% summarise(mean_hwy=mean(hwy))

df_mpg

ggplot(data=df_mpg,aes(x=drv,y=mean_hwy))
ggplot(data=df_mpg,aes(x=drv,y=mean_hwy))+geom_col()

#시간에 따른 그래프 
data("economics")
economics
#x축 시간을 의미하는 date
#y축 실업자수를 의미하는 unemploy 

ggplot(data=economics,aes(x=date,y=unemploy))+geom_line()

#상자 그래프

ggplot(data= mpg,aes(x=drv,y=hwy))
ggplot(data= mpg,aes(x=drv,y=hwy))+geom_boxplot()

#----------------------------------------------------------

# 문자열 관련 함수 
library(stringr)

#str_xxxx()

data <- "a12345 6789"

str_length(data) #공백 포함

str_sub(data,start=3,end=8)
str_sub(data,start = -3,end=-1) #e뒤에서 찾을 수 있음

letters #소문자
LETTERS #대문자 
letters[4:8] #소문자 알파뱃을 가지고 있음 
LETTERS[1:3]

str_c(letters[-26],"다음은",letters[-1])


str_c(letters,collapse=",") #문자 사이에 collapse 삽입하여 출력 

data2 <- c("무지개 색깔은 빨강, 주황, 노랑, 초록, 파랑, 남색, 보라","과일에는 딸기,바나나,망고,포도,배를 좋아합니다.")

data2

#, 단위로 분리
d3<- str_split(data2,pattern = ",")
d3

#data2 에서 과일만 뽑아내기 

data2[2]
str_sub(data2[2],start = 6 ,end=19)
str_split(str_sub(data2[2],start=6,end=19),pattern = ",")

id_list<-c("aaa,bbb,ccc,ddd,eee,fff")
#아이디만 추출

id <- str_split(id_list,pattern =",")
id

#str_dup(문자열, 반복횟수)

data3 <- c("소주","맥주","와인")
data3
str_dup(data3,3)
str_dup(data3,1:3)

# str_pad(문자열,문자열 너비,side=c("left,right","both"),pad="삽입문자")
# lpad() ==> lapd(sal,10,"*")
data4 <- 3000
str_pad(data4,10,side="left",pad="*")

data5<- 5000
str_pad(data5,10,side="right",pad="*")

data6<- 6000
str_pad(data6,10,side="both",pad="*")

# str_wrap(문자열,width="폭",ident="첫번째 오는 행의 여백",exdent="그외의 행의 여백")
d7 <-str_wrap("오늘은 수요일", width="20",indent=4,exdent=0)
d7


data5 <- "간장공장 공장장은 깐콩 공장 공장장"
word(data5,start =2 ,end=3)

#Hello Bigdata R world 문자열에서 
#Bigdata R 문자열만 뽑아서 출력 

data6 <- "Hello Bigdata R world"
word(data6,start=2,end=3)

#패턴매칭
# str_detect(문자열,찾고싶은문자)

str_detect(data5,"공")

data5[str_detect(data5,"공")]

str_count(data5,"공")

data6 <-c("aaa","bbb","123","aaa@aaa.com")
#@포함되어 있는 문자열을 탐색하고 해당 단어를 출력

str_detect(data6,"@")
data6[str_detect(data6,"@")]

data7 <-c("aaa","bbb","123","aaa@aaa.com")

# 숫자로만 구성되어 
str_extract(data7,"[0-9]+")

# @기호가 있는 문자만
str_extract(data7,"@")

# str_replace(문자열,매치할부분,치환할부분)
fruit <- c("one apple","two pears","three bananas")
# aeiou ==> - 

str_extract(fruit,"[aeiou]")
str_extract(fruit,"[aeiou]","-")


#data6 에서 이메일 형식을 찾고
#그중 id 부분만 출력 



data <- c("앞면","뒷면")
data

#복원 추출 
sample(data,10,replace =T)
plot(0,0,xlab ="동전던진횟수",ylab="앞면비율",xlim=c(1,5000),ylim=c(0,1))
ani.options(interval=0.05)
sum<-0
for (x in 1:5000){
  coin <- sample(data,1,replace =T)
  if(coin =="앞면"){
    sum<- sum+1
  }
  #앞면이 나온 비율
  prob <- sum/x
  points(x,prob)
  ani.pause()
  }

abline(a=0.5,b=0,col="red")

#몬테카롤로 시뮬레이션
#카지노로 유명한 모나코의 도시 
#무작위값, 난수를 이용하여 반복적 계산을 통해 확률적 값을 구하는 모형


#----------------------------------------

#무한 모집단 ==> 모평균,모분산(parameter)
#유한 

#표본 ==> 표본평균,표본분산

#동일분포를 가지는 분포들의 평균은 그 갯수가 많아지면 언제나 
#정규분포를 수렴한다. 

#척도별 기술 통계량
#대표값: 평균,합계,사분위수,최빈수 








#산포도 : 분산(varience),표준편차(standard deviation)
        # 최소, 최대


getwed()

data<- read.csv("descriptive.csv",header = T)
data

legth(data$gender)
summary(data$gender)  #명목척도 의미없음

table(data$gender)

x<- table(data$gender)


#비율 척도 변수의 기술통계량
length(data$cost)
summary(data$cost)

mean(data$cost)
#결측치 제거 outlier 제거 

plot(data$cost)

data<-subset(data,data$cost>=2 & data$cost <=10)
data
x <- data$cost
plot(x)
# cost 변수의 대표값 ---
# 평균
mean(x)
# 중위수
median(x)
# 오름차순
sort(x)
# 내림차순
sort(x,decreasing = T)
# 1사분위수 
quantile(x)
# 3사분위수

summary(x)

#cost 변수의 산포도
#분산
var(x)
#표준편차 
sd(x)
#최소값 
min(x)
#최대값
max(x)
#범위
range(x)


#척도 : 사물이나 사람의 특성을 수량화 하기 위해 
#체계적인 단위를 가지고 그 특성을 숫자로 부여한것 

# 연속형 시각화
table(data$cost)
hist(data$cost)

# 연속형 ==> 범주화 (리코딩):1,2,3

data$cost2[data$cost>=1 & data$cost<=3]<- 1 
data$cost2[data$cost>=4 & data$cost<=6]<- 2 
data$cost2[data$cost>=7]<- 3 

hist(data$cost2)
table(data$cost2)

length(data$cost2)

# 추정 : 표본을 통해서 모집단을 확률적으로 추측 
# 검정통계량 : 표본에 의해서 계산된 통계량 
# 표본평균, 표준편차 
# 모수 : 모집단에 의해서 나온 통계량( 모평균,모표준편차)
# 점추정 : 제시된 한개의 값과 검정통계량을 직접 비교하여 가설 기각 유무를 결정
# 중2학년 학생들의 평균키 160.0cm로 추정 
# 구간추정: 신뢰구간 과 검정통계량을 비교하여 가설 기각 유무를 결정 
# 신뢰구간 : 오차범위에 의해서 결정된 하한값과 상한값의 범위를 믿을 수 있는 구간 

x <- rnorm(1000, mean = 100 ,sd=10)
x

mean(x)

# 평균차이 검정
# 귀무가설 : 평균 95와 차이가 없다. 
# 대립가설(연구가설) : 평균95와 차이가 있다. 

# t-test 
# student 
# 흑맥주 생산에 필요한 보리 농장에서 보리 품질의 차이 
 
t.test(x,mu=95)
# t = 13.798, df = 999, p-value < 2.2e-16
# 95% 신뢰수준에서 98.82797 100.09737
# p-value < 2.2e-16  < 0.05
# 기무가설 기각 
# 대립가설 채택

#평균 95와 차이가 있다가 할 수 있다


# 평균 99.54 차이가 있는지?
# 가설 설정
# 귀무가설 : 평균 99.54와 차이가 없다
# 대립가설(연구가설) : 평균 99.54와 차이가 있다

t.test(x,mu=99.54, conf.lenve = 0.99)
# 
# t = -0.23909, df = 999, p-value = 0.8111
# p- value : probability value
# 의미가 있다 라고 말할 확률 
# 유의수준 : a , 유의 확률 p-value


