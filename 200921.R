#anscomebe's quartet

df_x <- read.csv(file = 'anscombex.csv', header = T, sep =',')
df_x

df_y <- read.csv(file ='anscombey.csv', header =T ,sep=",")
df_y

# x1 => y1 
# x1의 평균, 표준편차

mean(df_x$x1)
sd(df_x$x1)

apply(df_x,2,mean)
apply(df_x,2,sd)
apply(df_y,2,mean)
apply(df_y,2,sd)


par(mfrow=c(2,2))
barplot(apply(df_x,2,mean),ylim=c(0,11),main="mean of x")
barplot(apply(df_x,2,sd),ylim=c(0,5),main="sd of x")
barplot(apply(df_y,2,mean),ylim=c(0,11),main="mean of y")
barplot(apply(df_y,2,sd),ylim=c(0,5),main="sd of y")

#mbti
#상관관계

g1_cor <- cor(df_x$x1, df_y$y1)
g2_cor <- cor(df_x$x2, df_y$y2)
g3_cor <- cor(df_x$x3, df_y$y3)
g4_cor <- cor(df_x$x4, df_y$y4)

#cor.test

# lm(y~x)
g1_lm <- lm(df_y$y1~df_x$x1)
# y = 0.5001*x + 3.0001
g2_lm <- lm(df_y$y2~df_x$x2)
g3_lm <- lm(df_y$y3~df_x$x3)
g4_lm <- lm(df_y$y4~df_x$x4)

dev.new() #새로운 창 만들기 
par(mar=c(0.1,0.1,0.1,0.1)) #마진 넣어주기 
plot(0,type="n",xlim = c(0,7), ylim = c(0.5,4.5),ann=F,axes =F)
text(1,4,paste0("g1_cor=",round(g1_cor,2)),cex=1.3)
text(1,3,paste0("g2_cor=",round(g2_cor,2)),cex=1.3)
text(1,2,paste0("g3_cor=",round(g3_cor,2)),cex=1.3)
text(1,1,paste0("g4_cor=",round(g4_cor,2)),cex=1.3)

text(3,4,paste0("g1 intercept =",round(g1_lm$coefficients[1],2)),cex=1.3,col="red")
text(3,3,paste0("g2 intercept =",round(g2_lm$coefficients[1],2)),cex=1.3,col="red")
text(3,2,paste0("g3 intercept =",round(g3_lm$coefficients[1],2)),cex=1.3,col="red")
text(3,1,paste0("g4 intercept =",round(g4_lm$coefficients[1],2)),cex=1.3,col="red")


text(5,4,paste0("g1 slope =",round(g1_lm$coefficients[2],2)),cex=1.3,col="blue")
text(5,3,paste0("g2 slope =",round(g2_lm$coefficients[2],2)),cex=1.3,col="blue")
text(5,2,paste0("g3 slope =",round(g3_lm$coefficients[2],2)),cex=1.3,col="blue")
text(5,1,paste0("g4 slope =",round(g4_lm$coefficients[2],2)),cex=1.3,col="blue")


#산점도

par(mfrow= c(2,2))
plot(df_x$x1,df_y$y1 , col=rainbow(4)[1],pch=16,main="group1",xlab="X",ylab="y",xlim=c(0,20),
     ylim=c(0,12))
plot(df_x$x2,df_y$y2 , col=rainbow(4)[2],pch=16,main="group2",xlab="X",ylab="y",xlim=c(0,20),
     ylim=c(0,12))
plot(df_x$x3,df_y$y3 , col=rainbow(4)[3],pch=16,main="group3",xlab="X",ylab="y",xlim=c(0,20),
     ylim=c(0,12))
plot(df_x$x4,df_y$y4 , col=rainbow(4)[4],pch=16,main="group4",xlab="X",ylab="y",xlim=c(0,20),
     ylim=c(0,12))



#--------------------------------------------------------------------

#A식당의 배달시간 벡터 
storeA <- c(20,21,23,22,26,28,35,35,41,41,43,45,55,45,57,54,53,43,70,32,65,65,70)
#평균
mean(storeA)
median(storeA)


storeB <- c(5,6,7,11,23,54,20,30,40,30,20,23,34,23,43,30,34,37,40,44,50,51,70,600)
mean(storeB)
median(storeB)

# b에서 600보다 작은 값 선택
storeB[storeB<600]
# 그 값을 가지고 평균
mean(storeB[storeB<600])


#사분위수 
quantile(storeA)
quantile(storeB)

summary(storeA)
summary(storeB)

# 상자그림 그리기 
par(mar=1,1,1,1)
par(mfrow= c(1,1))
boxplot(storeA)
boxplot(storeB)
#이상치 제거 후 
#boxplot 그리기 
boxplot(storeB[storeB<600])
storeB <- storeB[storeB<600]

boxplot(storeA,storeB,names = c("A식당","B식당"))

#그려진 상자그림에 평균을 추가로 다시하기 

points(c(mean(storeA),mean(storeB)),pch=2,col="red",cex=2)

#c식당의 배달시간 벡터

storeC<- c(5,5,12,10,11,20,20,20,20,20,21,20,31,32,31,31,31,36,40,40,51,61,61,61,61,61,70)

#이상치 제거한 후에 storeB와 storeC를 비교할경우 어느가게를 선택할까요?
#측정값과 boxplot 그리고 판단

summary(storeC)
quantile(storeC)
mean(storeC)

par(mar=1,1,1,1)
par(mfrow= c(1,1))
boxplot(storeB,storeC,names = c("storeB","storeC"))
points(c(mean(storeB),mean(storeC)),pch=2,col="red",cex=2)

# b식당 히스토그램 그리기

par(mfrow=c(1,3))

hist(storeA,main="A식당 배달시간 분포",xlab="배달시간 구간",ylab="건수",col="red")
hist(storeB,main="B식당 배달시간 분포",xlab="배달시간 구간",ylab="건수",col="blue")
hist(storeC,main="C식당 배달시간 분포",xlab="배달시간 구간",ylab="건수",col="yellow")


var(storeB)
var(storeC)

sd(storeB)
sd(storeC)

#범주형 데이터
#혈액형 : A,B,AB,O RH- RH+
#우리반 학생들의 혈액형
bloodtype <-c('B','O','O','O','O','A','A','B','A','B','B','A','A','A','B','O','A','AB')

bloodtype
# 총몇명
length(bloodtype)
#빈도
table(bloodtype)

#
table_bloodtype<-table(bloodtype)
table_bloodtype

#더하려고 빈도를 구한 후 sum 사용 
names(table_bloodtype)
sum(table_bloodtype)
# addmargins(table(bloodtype))
#파이 차트 생성
pie(x=table_bloodtype)

pie(x=table_bloodtype,labels = c("A형","AB형","B형","O형"),col=c("chocolate1","chartreuse2",
                                                             "darkgoldenrod1","darkorchid1"),
    lty=2,main="우리반 혈액형 분포")

colors()

#barplot()

# barplot(bloodtype)
barplot(table_bloodtype)


#------------------------------------

#데이터 분석 종류
#1.기술적 데이터 분석 
#주어진 데이터를 요약/집계하여 현재 모습을 묘사/기술하는 것이 목표
#2.탐색적 데이터 분석 (EDA)
#여러 변수 간의 관계, 패턴, 트랜드 찾는다. 
#데이터 분석 초기에 가설 수립 


#3. 확증적 데이터 분석 (CDA)
#도출된 가설을 검증한다. 
#

#4. 예측적 데이터분석(PDA)
#발생하지 않은 어떤 사건에 대한 예측 

#탐색적 데이터 분석
dataset<-read.csv(file = "dataset.csv",header =T,sep=",")

#구조 확인 
str(dataset)

# resident , gender, job, age, position,price,suvery
# 거주지,성별,직업,나이,직위,구매금액,만족도

View(dataset)
head(dataset)
tail(dataset)
dim(dataset)
names(dataset)
attributes(dataset)

#나이 
dataset$age
dataset$resident

length(dataset$age)
plot(dataset$price)

x<-dataset$gender
x
y<-dataset$price
y

dataset$gender
dataset["gender"]

dataset[2] #두번째 컬럼
dataset[6]

#3번째 관측치 행 전체
dataset[3,]
#5번째 변수(열) 전체
dataset[,5]
#job,price 두개의 변수
dataset[c("job","price")]
#100~110행까지 전체
dataset[c(100:110),]

summary(dataset$price)

sum(dataset$price)

sum(dataset$price,na.rm = T)

price2<-na.omit(dataset$price)
price2
length(price2)
sum(price2)

# 극단치 발견과 정제

dataset$gender
# 1,2 만 선택
# %>% : pipe 연산자
# 함수를 계속 중첩
# gender 1, 2 선택
library(dplyr)
data <- dataset %>% filter(gender==1|gender==2)
data

data2<-subset(dataset,dataset$gender==1|dataset$gender==2)
data2

#앞에서 6개만 출력 
head(data,6)
head(data2,6)
#gender 히스토그램, 파이 차트 그리기
par(mfrow=c(1,1))
pie(table(data$gender),labels = c("남성","여성"),col=rainbow(2),main="성별")
hist(data$gender)

plot(dataset$price,ylim = c(0,10))

data <- dataset %>% filter(price >=2 & price<=10)
data
length(data3)

#줄기와 잎 도표 보기
stem(data$price)


#설문
#만족도 조사
data$survey
# 1 매우 좋음 ==> 5
# 5 매우 나쁨 ==> 1
#역코딩 

survey <- data$survey
# 1=>5 , 2=>4 3=>3,4=>2,5=>1
curvey <- 6- survey #척도+1 값을 빼줌 
curvey
#10점 척도라 11을 빼줌 

data$survey <- curvey
head(data)
data$age
#성인 고객 
#20~70


age2 <-data %>% filter(age>=20 & age<=70)
age2

data$age2 <- age2


pos <- data$position
tpos <- 6-pos
tpos
data$position<-tpos

#age 변수 NA <= 평균 
mean(data$age ,na.rm=T)
is.na(data$age) #is.na() 로 NA 인지 여부를 판단

data$age[is.na(data$age)] <- 42.6

mean(data$age) # na.rm = T 하지 않아도 평균을 구할 수 있음


data$age[data$age <=30]


data$age2[data$age <=30] <- "청년층"
data$age2

data$age2[data$age >30 & data$age<=45]<-  "중년층"
data$age2[data$age>45]<-  "장년층"

data$age2

data$resident
# 1.서울 2~4 광역시 5 시구군 
data$resident2 #특별시 , 광역시 , 시구군 

range(data$resident,na.rm=T)

data$resident2[data$resident ==1]<- "서울"
data$resident2
data$resident2[data$resident ==2 |data$resident ==3|data$resident ==4]<- "광역시"
data$resident2[data$resident ==5]<- "시군구"

data$resident2


data$gender2[data$gender==1]<-"남자"
data$gender2[data$gender==2]<-"여자"

data$gender2
table(data$age2)/sum(table(data$age2))*100

#소수점 2자리에서 반올림 

label <- paste(data$age2,"\n",round(table(data$age2)/sum(table(data$age2))*100,2),"%")

pie(table(data$gender2),labels = label)


# 나이별 빈도를 파이 그래프로 그리세요 

table(data$age2)
pie(table(data$age2))


# 데이터 정제 작업이 끝나면 해당데이터를 저장한다

write.csv(data,"cleanData.csv",quote =F , row.names = F)

#-------------------------------------------------

install.packages("rvest")
library(rvest)
url<-"https://search.shopping.naver.com/detail/detail.nhn?cat_id=50000440&nv_mid=14138313311&query="
# https://search.shopping.naver.com/detail/detail.nhn?cat_id=50000440&nv_mid=14138313311&query=%EB%AC%BC%EA%B4%91%ED%81%AC%EB%A6%BC&bt=2&frm=NVSCPRO&NaPm=ct%3Dkfc556m0%7Cci%3Da9c959c54220d035e3f846f7e97b4e0f3a7c97c7%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D23a13861b221cdbb80166b284dbfa1c014739156

url
keyword<-"물광크림"
keyword<-URLencode(keyword) #URL 코드로 변경

url2 <- paste0(url,keyworld)
url2

txt<- read_html(url2)
txt
#container > div.summary_area > div.summary_info._itemSection > div > div.h_area > h2

txt2 <- txt %>% html_node("div > div.h_area > h2") %>% html_text()
txt2

#content > div > div.summary_cet > div.price_area > span > em
txt3 <- txt %>% html_node("div > div.summary_cet > div.price_area > span > em") %>% html_text()
txt3


#--------------------------------네이버 뮤직 ---------------------------------------------------------

url3<-"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%9D%8C%EC%95%85&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84%EC%9D%8C%EC%95%85&tqi=U2mgJdp0Yihss63EPsNssssstm8-488294"

txt4<-read_html(url3)
txt4


naver_songN <- txt4 %>% html_node(" li:nth-child(1) >div > div.music_area > div.music_info > div.title > a") %>% html_text()
naver_songN

naver_songS <-txt4 %>% html_node("  li:nth-child(1) >div > div.music_area > div.music_info > div.info > a.singer") %>% html_text()
naver_songS

naver_songA <-txt4 %>% html_node(" li:nth-child(1) > div > div.music_area > div.music_info > div.info > a.album") %>% html_text()
naver_songA

naver_songAre <-txt4 %>% html_nodes("div.music_area")
naver_songAre

for(i in naver_songAre){
cat(i %>% html_node("div.music_info > div.title > a") %>% html_text()
    ,i %>% html_node("div.music_info > div.info > a.singer") %>% html_text()
    ,i %>% html_node("div.music_info > div.info > a.album") %>% html_text(),"\n")
# cat(i %>% html_node("div.music_info > div.info > a.singer") %>% html_text(),"\n")
# cat(i %>% html_node("div.music_info > div.info > a.album") %>% html_text(),"\n")

}


list <- NULL
for (i in c(1:10)){
  naver_song <- txt4 %>% html_node(paste("li:nth-child(",i,") > div > div.music_area > div.music_info > div.title > a"))%>% html_text()
  naver_singer<- txt4 %>% html_node(paste("li:nth-child(",i,") > div > div.music_area > div.music_info > div.info > a.singer"))%>% html_text()
  naver_album <- txt4 %>% html_node(paste("li:nth-child(",i,") > div > div.music_area > div.music_info > div.info > a.album"))%>% html_text()
cat("\n","제목 :",naver_song,"\n","가수 :",naver_singer,"\n","앨범 :",naver_album,"\n","---------")

list <- c(list,naver_song,naver_singer,naver_album)
}

matrix(list,ncol = 3,byrow = T)

library(httr)

url = 'https://www.melon.com/chart/'
get_url = GET(url) #get 방식으로 서버에 접근근
get_url
my_html<-read_html(get_url,encoding = 'utf-8')
my_html


vsong <- NULL
vsinger <- NULL
valbum <- NULL

for (i in c(1:10)){
  naver_song <- txt4 %>% html_node(paste("li:nth-child(",i,") > div > div.music_area > div.music_info > div.title > a"))%>% html_text()
  naver_singer<- txt4 %>% html_node(paste("li:nth-child(",i,") > div > div.music_area > div.music_info > div.info > a.singer"))%>% html_text()
  naver_album <- txt4 %>% html_node(paste("li:nth-child(",i,") > div > div.music_area > div.music_info > div.info > a.album"))%>% html_text()
  cat("\n","제목 :",naver_song,"\n","가수 :",naver_singer,"\n","앨범 :",naver_album,"\n","---------")
  
  vsong[i] <- naver_song
  vsinger[i] <- naver_singer
  valbum[i] <- naver_album
  
}

vsong
vsinger
valbum

df<-data.frame(vsong,vsinger,valbum)
df

str(df)

write.csv(x = df , file = "singer.csv",quote =F, row.names = F,fileEncoding = "UTF-8")



# 애플리케이션 정보
# Client ID	
# 8WV5lNCZj94ZpxlZ_Lps
# Client Secret	
# VD5nxtqYD5
