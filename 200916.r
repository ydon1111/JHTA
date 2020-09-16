#table.txt 파일을 읽어오기 

txtemp <- read.table(file = "table.txt", header = T ,sep = "\t")
txtemp


#csv 파일 읽어오기 
#emp2.csv
csvemp <- read.table(file = "emp2.csv",header = F , sep=",")
csvemp

#첫줄만 빼고 출력 
csvemp <- csvemp[-1,]
csvemp
csvemp$V6
#순서형 데이터 
pay <- ordered(csvemp$V6,c(1:5000))
class(pay)

#순서형인지 여부 리턴
is.ordered(pay)
#순서형은 평균을 낼 수 없음 
#숫자로 형편환
pay <- as.numeric(pay)
mean(pay)

#벡터로 데이터 프레임 만들기

#상품 가격 판매수량 
#딸기 5000 300
#사과 3000 800
#배   4000 1000
#키위 2000 3000


name <- c("딸기","사과","배","키위")
price <- c(5000,3000,4000,2000)
qty <-c(300,800,1000,3000)


df <- data.frame(name,price,qty)
df

colnames(df)
colnames(df) <- c("상품이름","가격","판매수량")
df

mean(df$가격)

# y = x*2 
x <- c(1,2,3,4,5)
y <- c(2,4,6,8,10)

df2 <- data.frame(x,y)
df2

hist(df2$x)

#산점도 그리기 
plot(df2$x)
plot(df2$y ~ df2$x)
#    y축     x축 

#사원 급여 빈도를 산점도로 그려보기 

plot(txtemp$SAL ~ txtemp$JOB)


# I/O
x <- scan()
x
mean(x)

#문자입력

y <- scan(what="")
y


df = data.frame()
df
df<-edit(df)
df

getwd()

student <- read.table(file ="student.txt" , header = F)
student

colnames(student) <- c("id","name","height","weight")
student

student1 <- read.table(file ="student1.txt", header = T)
student1

# 구분자가 있다면 ? 파일 불러오기

student2 <- read.table(file = "student2.txt", header = T ,sep =";")
student2

student3 <- read.table(file = "student3.txt", header = T , na.strings = c("-","&"))
student3


#student2 객체의 키의 평균
mean(student2$키)

#student3 객체의 키의 평균
mean(student3$키)

#결측치를 제외한 키의 평균
mean(student3$키, na.rm = T)


#student4.txt 파일 읽기
#file.choose() <- 파일 직접 선택하기(팝업창이 나옴)
student4 <- read.table(file.choose(),header = T, sep = ",",na.strings = "-")
student4


#xlsx 
Sys.getenv()

# 자바의 설치경로  
Sys.setenv(JAVA_HOME="C:\\Program Files\\Java\\jdk1.8.0_261")

#패키지 설치 
install.packages("rJava")
install.packages("xlsx")
library(rJava)
library(xlsx)
studentex <- read.xlsx(file.choose(),sheetIndex = 1,encoding = "UTF-8")
studentex
class(studentex)
# data.frame 을 파일로 저정 
write.csv(studentex, file = "df_st.csv")

# Rdata 
save(studentex, file ="st.rda")
# 메모리에서 studentex 데이터프레임을 제거 

rm(studentex)
load("st.rda")

# emp2.csv 파일을 읽어와서 emp라는 dataframe 을 생성
#구조확인,몇행 몇열짜리인지?
#앞부분 몇개만 확인
#뒤쪽으로 몇개만 확인

emp <- read.csv(file = "emp2.csv",header = F ,sep=",")
emp
dim(emp)
str(emp)
head(emp,3)
tail(emp,3)
View(emp)

#summary 이해가 필요함 
summary(emp)

boxplot(emp$V6)

#emp.rda 저장 
save(emp,file="emp.rda")
#메모리에서 emp제거
rm(emp)
#파일로부터 읽기 
load("emp.rda")
emp


#emp3.xls
member <- read.xlsx(file = "emp3.xls",header = T,sheetIndex = 2,encoding = "UTF-8")
member
dim(member)

#처음 12개의 데이터를 출력
head(member,12)
#마지막 10개 데이터를 출력
tail(member,10)
#요약정보
summary(member)
#수학점수 ??? 요약정보를 보고 간단히 정리 
summary(member$mat)
#최소,최대,제1사분위수값, 중위수값, 평균
20,95,20,90,59.17
#3사분위수값 
90
#수학점수 :boxplot
boxplot(member$mat)
#각 점수별로 행/열 방향으로 max 값 구하기 
apply(member[-1],1,max)
apply(member[-1],2,max)

#각 점수의 평균,분산,표준편차 구하기 
apply(member[-1],2,mean)
apply(member[-1],2,var)
apply(member[-1],2,sd)

#m1에 총점을 계산해서 새로운 변수로 추가하기 
m1 <- apply(member[-1],1,sum)
m1
member$Total <- m1 
member
#avg변수 추가 
member$Avg <- member$Total/3
member
#memberdata.csv로 m1객체저장 
save(member, file ="memberdata.csv")



z <- x*y 
z
cat("x*y의 결과는",z,"입니다. \n")#\n 줄바꿈
cat("x*y = ",z)

#print() 함수
print(z) #변수 , 수식만 가능
print(z*10)
#print("x*y =".z) #Error
z

# 2.파일저장
#read.table()
student<-read.table(file = 'student.txt')
#기본옵션 행이름, 열의 이름 따옴표로붙음
write.table(student,"stdt.txt")
#행이름 제거하고 저장
write.table(student,"stdt2.txt",row.names = F)

# "" 제거하고 저장
write.table(student,"stdt3.txt",row.names = F,quote = F)

#열이름 제거하고 저장
write.table(student,"stdt4.txt",row.names = F,quote =F ,col.names = F)

#csv 파일 읽기
#read.csv(),write.csv()
library(xlsx)
st_df <- read.xlsx(file.choose(),sheetIndex = 1,encoding = "UTF-8")
st_df

write.xlsx(st_df,"studentx.xlsx")
#csv 파일로 행이름 ,"" 제거: stdf.csv
write.csv(st_df,"stdf.csv",quote = F)
#

movie <- read.csv(file = "movie.csv")
movie
write.table(movie,"movie.xlsx")
dim(movie)



#제어문 

#학점구하기 
score<-scan()
score

#만약 90점이상이면 A 
if (score>90){
  result="A"
}else if(score>=80){
  result="B"
}else if(score>=70){
  result="C"
}else if(score>=60){
  result="D"
}else{
  result="F"
}
cat("당신의 학점은",result)


#사용자로부터 숫자를 입력 받아
#그 값이 홀수인지 짝수인지 판별하고자 한다
#코드로 작성하세요

num <- scan()
num

if (num%%2 == 0){
  result ="짝수"
}else{
  result ="홀수"
}
cat(result)

#3항연산자 
# ifelse(조건,참,거짓)

#80이상이면 우수 아니면 노력 
ifelse(score>=80, "우수","노력")
#90이상이면 a 아니면 f 
score <- scan()
ifelse(score>=90,"A",
       ifelse(score>=80,"B",
              ifelse(score>=70,"C",
                     ifelse(score>=60,"D","F")
                     )
              )
)

#excel.csv
excel<-read.csv(file = "excel.csv", header = T,sep=",")
excel       
str(excel)
q1<-excel$q1 
q1
#4보다 큰 경우 루트 :sqrt
ifelse(q1>4,round(sqrt(q1)),q1)

#1과 5만 출력 , 그외 나머지 지수승
ifelse(q1>=2 & q1<=4,q1^2,q1)

ifelse(q1==1 | q1==5 ,q1 ,q1^2)


#switch 문
#switch(비교구문,실행구문1,실행구문2,실행구문3)

switch("pwd",id="hong",pwd="1234",age=20,name="홍길동")


#which 문
#which()괄호내에 조건에 해당하는 위치(인덱스)를 출력 

name <-c("kim","lee","park","choi")
which(name=="kim")

no<-c(1:5)
name <- c("BTS","엑소","블랙핑크","에이핑크","트와이스")
score <- c(99,98,90,89,85)
exam <- data.frame(학번=no,이름=name,성적=score)
exam

#bts는 몇번째
which(exam$이름 =="BTS")
#90점 이상인 사람들의 위치 

which(exam$성적>=90)
exam[c(which(exam$성적>=90)),]

#90점 이상인 그룹의 이름만 출력 
exam[which(exam$성적>=90),2]

#emp3.xls 파일을 읽어온다.
#dataFrame을 만든다. (emp)
#수학성적이 90점 이상인 사람의 위치를 알아온다.
#해당위치의 행을 가져온다. 
#여러열중 name 열만 출력한다.

emp <-read.xlsx(file = "emp3.xls",sheetIndex = 2,encoding = "UTF-8",header = T)
emp
class(emp)

which(emp$mat>=90)
emp[which(emp$mat>=90),]
emp[which(emp$mat>=90),1]

df<-data.frame(var1=c(1,2,3),var2=c(6,7,8))
df

#사본
df_cp <- df 
df_cp

#열의 이름변경 var1 ==> y1 var2==> y2
df_cp

colnames(df_cp) <- c("y1","y2")

names(df_cp)<- c("y1","y2")
df_cp


#rename : dplyr 패키지의 rename()
#rename(dataframe, new변수 = old변수,....)
install.packages("dplyr")
library(dplyr)
df<-rename(df,y1=var1)
df<-rename(df,y2=var2)
df

##ggplot2패키지에 있는 mpg데이터 실습 
install.packages("ggplot2")
library(ggplot2)

sessionInfo()
data(mpg)
mpg

#특정패키지에 들어있는 함수나 데이터를 지칭 ::

#메모리있는 변수 전체제거
rm(list=ls())

mpg<-as.data.frame(ggplot2::mpg)
mpg
str(mpg)
#1999년 ~ 2008년 사이에 38개 유명모델의 연비데이터
#manufacturer : 제조회사
#modle :모델명
#displ : 배기량
#cyl: 실린더 갯수
#drv: 구동방식 
#hwy: 고속도로 연비
#class :자동차 종류
#trans : 변속기 종류
#cty : 도시연비
#fl: 연로종류 

#cty ==>city
#hwu ==>highway
#fl ==>fuel_type

mpg <-rename(mpg,city=cty)
mpg <-rename(mpg,highway = hwy)
mpg <-rename(mpg,fuel_type = fl)
str(mpg)

#통합연비 total : 파생변수 
mpg$total <- (mpg$city+mpg$highway)/2
mpg$total

#앞데이터 6개만 출력
head(mpg)
#total 변수의 요약정부
summary(mpg$total)

hist(mpg$total)
#합격판정 : 20이상 pass
#fail 

mpg$test<-ifelse(mpg$total>20,"pass","fail")
mpg

#등급 30 a , 25 b,  c 
mpg$grade<-ifelse(mpg$total>=30,"a",ifelse(
       mpg$total>=25,"b",ifelse(mpg$total>=20,"c","d")
       ))

mpg

#구조
#데이터 앞에서 6개만 출력 
head(mpg,6)


View(mpg)
