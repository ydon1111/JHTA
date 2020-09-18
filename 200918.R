# 이산형 변수 
# 정수 단위로 나누어 측정할 수 있는 변수 
# 시각화 방법 : 막대차트 , 점차트 ,파이 차트 

# 연속형 변수 
# 시간. 길이 등과 같이 연속성을 가진 실수단위 변수 
#시각화 방법: 히스토그램, 상자그래프, 산점도, 변수간의 비교 시각화 

library(RSADBE)


help("RSADBE")

data("Severity_Counts")
str(Severity_Counts)
class(Severity_Counts)
#버그 측정 데이터 셋 

head(Severity_Counts)

?barplot
barplot(Severity_Counts, ylim = c(0,13000), col = rainbow(10),main="소프트웨어 버그 측정결과", font.main=3)



barplot(Severity_Counts,xlab = "Bug Count", xlim = c(0,12000),horiz = T, col = rep(c(6,5),5))

#1.검정 , 2. 빨강 , 3. 초록 , 4. 파랑 , 5. 하늘색 , 6. 자주색, 7.노랑색 

data("Bug_Metrics_Software")
Bug_Metrics_Software
#5개의 소프트웨어 별로 발표전과 후 버그 측정 결과를 3차원 배열 구조로 제공
# 1면 (발표 전), 2면(발표 후)

str(Bug_Metrics_Software)

par(mfrow=c(1,2))

#발표전
barplot(Bug_Metrics_Software[,,1],beside=T, col = c("lightblue","mistyrose","lightcyan","lavender","cornsilk"),
        legend = c("JDT","RDE","EQUINOX","LUCENE","MYLYN"),font.main=4, main= "B" )


#발표후 
barplot(Bug_Metrics_Software[,,2],beside=F,col=c("lightblue","mistyrose","lightcyan","lavender","cornsilk"),
        legend = c("JDT","RDE","EQUINOX","LUCENE","MYLYN"),font.main=4, main= "A" )



par(mfrow=c(1,1))

dotchart(Severity_Counts,pch=1:2,lcolor = "red", labels = names(Severity_Counts))


class(Severity_Counts)

#파이차트

par(mfrow=c(1,2))

pie(Severity_Counts[c(1,3,5,7,9)])
title("BEFORE")

pie(Severity_Counts[c(2,4,6,8,10)])
title("AFTER")


#RSADBE 패키지에서 제공되는 데이터셋

data("resistivity")
class(resistivity)
resistivity
#전선의 저항률 

#상자 그래프 
boxplot(resistivity,range=0)
boxplot(resistivity,range=0,notch=T)
#중위수 비교 
abline(h=0.140, lty=3)
abline(h=0.149, lty=3)



install.packages("psych")
library(psych)
data(galton)
galton

# 자식과 부모의 키 사이 관계 

par(mfrow=c(1,2))
hist(galton$parent, xlab = "Height to parent",col="mistyrose")

hist(galton$child, xlab = "Height to child",col="magenta")


par(mfrow = c(1,1))
#산점도 시각화
price <- runif(100,min=1 , max=100)
price
plot(price)
par(mfrow=c(2,2))   # 2행 2열 차트 
plot(price,type="l") #실선
plot(price,type="o") #원형과 실선
plot(price,type="h") #직선
plot(price,type="s") # 꺽은선

par(mfrow=c(2,3))
plot(price,type="o",pch=5)
#빈 사각형
plot(price,type="o",pch=15)
#채워진 마름모
plot(price,type="o",pch=20,col ="blue")
#Character Expension
plot(price,type="o",pch=20,col ="orange",cex=1.5)
plot(price,type="o",pch=20,col ="orange",cex=2.5, lwd=3)


#lwd : line width 

# sales.csv 파일
sales <-read.csv(file = "sales.csv",header = T , sep = ",")
sales

str(sales)

par(mfrow=c(1,1))
attach(sales)

# axes = F  x축 y축 눈금 제거 
# ann = F 축의 이름 제거 

plot(Quarter, A, type ="o", pch = 18 ,col = "blue",ylim=c(0,2500),axes = F ,ann =F)
axis(1,at=1:4, labels = c("1분기","2분기","3분기","4분기"))
axis(2,ylim=c(0,2500))
par(new=T)
text(3.7,2100,"사업부 A", cex=0.8)
title(main="사업부 2015년 분기별 매출추이 비교",col.main="red",font.main=4)
par(new=T)
plot(Quarter, B , type="o",pch=18,col="red",ylim=c(0,2500),axes=F,ann=F)
text(3.7,900,"사업부 B", cex=0.8)
par(new=T)
plot(Quarter, C , type="o",pch=18,col="green",ylim=c(0,2500),axes=F,ann=F)
text(3.7,600,"사업부 C", cex=0.8)
par(new=T)
plot(Quarter, D , type="o",pch=18,col="orange",ylim=c(0,2500),axes=F,ann=F)
text(3.7,300,"사업부 D" , cex=0.8)
#2행 3열
#각 분기별 상품 판매량을 출력
#색상 빨간색, 채워진 마름모
#서울 5두께
detach(sales)


galton
#x변수 , y변수 
#plot(x,y)
#plot(y~x)

plot(child~parent,data = galton, ylim=c(45,90),xlime=c(50,90))

#linear Regression : lm <== 선형회귀 확인 
out = lm(child~parent, data=galton)
abline(out,col="red")

#동일 데이터가 겹친 경우 

x=c(1,2,3,4,2,4)
y=rep(2,6)
x
y
plot(x,y)
table(x,y)
# 빈도를 df 
xy_df <- data.frame(table(x,y))
xy_df

plot(y~x,pch="@",cex=0.5*xy_df$Freq,col="red")

table(galton$child,galton$parent)

df2<- data.frame(table(galton$child,galton$parent))

df2


str(df2)

names(df2) <- c("child","parent","freq")
parent<-as.numeric(df2$parent)
child<-as.numeric(df2$child)
jpeg("galton.jpg",width = 720,height = 480)
plot(child~parent,pch="@",col="blue",cex=0.1*df2$freq,xlab="parent",ylab="child")

#iris 데이터셋
# 3가지 꽃의 종류별로 50개씩 
# 150개 관측치
#붓꽃에 관한 데이터 5개의 변수로 제공

iris
str(iris)

# Sepal.Length : 꽃받침의 길이
# Sepal.Width : 꽃받침의 너비 
# Petal.Length  :꽃잎의 길이
# Petal.Width : 꽃잎의 너비 
# Specise : 꽃의 종류 


ris 데이터 테이블을 대상으로 plot()함수를 이용하여  다음 조건에 맞게 차트를 그리시오.

1. 1번 컬럼이 x축, 3번 컬럼을 y축으로 차트 그리기
plot(iris[,1],iris[,3])

2. 5번 컬럼으로 색상 지정하기

plot(iris[,1],iris[,3], col =iris[,5])
3. 제목 추가("iris 데이터 테이블 산포도 차트")
plot(iris[,1],iris[,3], col =iris[,5],main ="iris 데이터 테이블 산포도 차트")
4. 파일로 차트 저장하기("E:/dev/Rworkspace/iris.jpg")


dev.off()

library(dplyr)

고객 리스트 데이터 프레임을 사용해서 아래의 작업을 처리하세요 

cust <- data.frame(age = 30:50, sales = rep(c(65,60,80),7))
freq <- rep(c(3,7,4,2,1,1,2),3)

sales는 각 고객별 총판매금액이고  freq는 구매횟수이다.


문제5: 고객의 수를 계산하세요

nrow(cust)


문제6: 고객의 나이를 큰값에서 작은 값의 순서로 정렬하세요

cust <- cust %>% arrange(desc(age))
cust

문제7: 고객의 나이 중 두번째로 큰 값은 얼마인가요?

cust[2,]
  
문제8: sales의 평균값은 얼마?

mean(cust$sales)

문제9: 각 고객별로 sales와 전체고객의 sales 평균간의 차이는 얼마?


cust$meangap <- round(abs(cust$sales-mean(cust$sales)))
cust
var(cust$sales)

문제10: cust dataframe에 freq를 걸럼으로 추가한 후 처음부터 3명의 고객을 출력하라.

cust$freq <- freq
head(cust,3)

문제11: 고객별 구매1건당 평균 sales 금액을 구하여 avgsales 라는 이름의 컬럼으로
cust dataframe에 추가한 후 마지막 두 명의  고객을 출력하라.

cust$avgsales <- round(cust$sales/cust$freq,2)
cust
tail(cust,2)

문제12 : cust dataframe을 avgsales 순서로 정렬하고, avgsales가 가장 큰 세명의 고객을 출력하라.

cust <- cust %>% arrange(desc(avgsales))
head(cust,3)

문제13: 고객의 freq와 sales간의 분포를  plot으로 작성하라.

plot(cust[,2], cust[,3])


