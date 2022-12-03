library(rJava)
library(xlsx)
movie <- read.csv(file= 'movie.csv',header =T )
movie
str(movie)

emp <- read.xlsx(file = "emp3.xls", sheetIndex=2 , encoding = "UTF-8")
emp
emp$total <- emp$kor + emp$eng + emp$mat
str(emp)
emp$avg <- round((emp$kor + emp$eng + emp$mat)/3,2)
head(emp,3)


ifelse(emp$avg>=90,"A","F")
emp$grade<- ifelse(emp$avg>=90,"A",
       ifelse(emp$avg>=80,"B",
              ifelse(emp$avg>=70,"C",
                     ifelse(emp$avg>=60,"D","F"))))
emp

hist(emp$avg)
#grade 
#if (조건){
#  문장1;
#}else if(조건){
#  문장2;
#}else{
#  문장3;
#}
str(emp)
emp$class <- seq(1,6,1)
emp$class <- rep(c(1:6),14)
emp$class

#1반 학생들의 데이터만 추출 
which(emp$class==1)
emp[c(1,2),]
emp[which(emp$class==1),]


library(dplyr)
# emp에서 반열의 값이 1과 같은 데이터만 추출 
emp %>% filter(class ==1) 

# 4,5,6 반 학생들 데이터만 추출 

which(emp$class == 4 | emp$class ==5 | emp$class ==6)
emp[which(emp$class == 4 | emp$class ==5 | emp$class ==6),]

# 2방식
emp %>% filter(class==4|class==5|class==6)

#3반만 빼고 데이터 추출 

emp %>% filter(class !=3)

# 수학점수가 50점 이하는 제거
emp %>% filter(mat>50)


#영어수학점수가 50점 이하인 학생들만 추출 

emp %>% filter(eng<=50 & mat<=50)
# 2,4,6반 학생들만 추출 
emp %>% filter(class ==2 | class==4|class ==6)
emp %>% filter(class %in% c(2,4,6))
emp %>% filter(class %in% seq(2,6,2))

#3반 학생들이 수학 총점과 평균 
which(emp$class ==3)
sum(emp[which(emp$class ==3),4])
mean(emp[which(emp$class ==3),4])
round(mean(emp[which(emp$class ==3),4]),2)

class3<-emp %>% filter(class ==3)
class3
sum(class3$mat)
mean(class3$mat)
round(mean(class3$mat))

# 6반 학생들의 영어총점과 평균 ?
class6 <- emp %>% filter(class ==6)
sum(class6$eng)
round(mean(class6$eng),2)

#특정변수만 선택하기
#영어 점수만 선택 

emp$eng 
# SELECT eng FROM emp 
emp %>% select(eng)
# class , 수학점수 
emp[,c(2,3)]
emp %>% select(class,mat)

#국어만 빼고 선택 
emp %>% select (-kor)

# 3반 학생들의 국어점수만 선택
emp[which(emp$class == 3),2]

class3 <-emp %>% filter(class==3)
class3 %>% select(kor)

emp %>% filter(class==3) %>% select (kor)

#10개만 보기 

head(emp,10)

emp %>% head(10)

#수학점수 앞에서 12개만 추출
#3반 학생들의 영어와 수학점수를 5개만 추출 

emp %>% select(mat) %>% head(12)

emp %>% filter(class==3) %>% select(mat,eng) %>% head(5)


#정렬 
#국어 성적이 낮은 순으로 출력
emp %>% arrange(kor) #오름차순 

emp %>% arrange(desc(kor)) #내림차순 

#select * from emp
#order by kor , eng ;

emp %>% arrange(kor, eng)

# 3반 학생들의 국어,영어,수학 class를 구하고 
#영어점수가 50점 이상 수학점수가 70점 이상 
#학생들의 데이터를 국어, 수학,영어 내림차순으로 
#정렬해서 3개만 출력 

emp %>% filter(class==3) %>% select(kor,eng,mat,class) %>% filter(eng>=50 & mat>=70) %>% arrange(desc(kor)) %>% head(3)

member <- emp %>% select (name,kor,eng,mat, class)           
member

#member <--- 총점 추가 
member <- member %>% mutate(total=kor+eng+mat)
member 

member <- member %>% mutate(avg =member$total/3)
member


#영어 점수의 합계
member %>% summarise(sum_eng = sum(eng))
member
#반별 영어 점수의 평군

#select avg(eng) from emp group by class

m <- member %>% group_by(class) %>% summarise(avg_eng=mean(eng))
m
write.csv(m,file="avg.csv",row.names = F,fileEncoding = "UTF-8")


#수학점수 60점 이상 5,6반 학생들의 이름, 영어 ,수학 ,평균점수를 구해 m2.csv 파일로 저장 
member
k <- member %>% filter(mat>=60) %>% filter(class %in% c(5,6)) %>% group_by(class) %>% summarise(avg_mat=mean(mat),avg_eng=mean(eng)) 


k
write.csv(k,file="m2.csv",row.names = F ,fileEncoding = "UTF-8")



#반복문 
n <- c(1:10)
n

n*10
#for i in range(10):
#
for (i in n){
  if(i%%2 ==0){
    print(i)
  }
}

for (i in n){
  if(i%%2 ==0){
    print(i)
  }
}
    
n <- c(1:9)
n
for (i in n){
  cat("3 *",i,"=", i*3,"\n")
}

i = 0 
while (i<10){
  i<- i+1
  print(i)
}

i= 0
while (i<9){
  i<- i+1
  cat("3 *",i,"=", i*3,"\n")
}


#repeat{}

cnt<-1 
repeat{
  print(cnt)
  cnt<- cnt+1
  #탈출조건
  if (cnt>20) break
}


cnt<-0
repeat{
  cnt<- cnt+1
  cat("3 *",cnt,"=", cnt*3,"\n")
  if(cnt>8)break #cnt == 9
  
}


# 1부터 100 사이의 정수 중 2의 배수를 출력 
# 3의 배수는 제외 repeat 

cnt <- 101 
repeat{
  cnt <- cnt-1
  if(cnt%%2==0){
    if(cnt%%3==0) next  #파이썬 continue와 같음 
    cat(cnt,"\n")
  }
  if(cnt==1) break
}


#---------------------------------------------------------------
#함수 

#function(매개변수){
#  명령1;
#}

f1<- function(){
  cat("매개변수가 없는 함수")
}

#함수호출
#함수명(인자,인수,파라미터)
f1() 

#매개변수가 있는 함수 
f2 <- function(x){ #가인수
  cat("x의 값 :",x,"\n")
}

f2(100) #실인수 

gugudan <- function(x){
  i = 0
  while(i<9){
    i <- i +1
    cat(x,"*",i,"=",x*i,"\n")
  }
}

gugudan(7)


#emp2.csv
emp2<-read.csv(file = "emp2.csv",header = F,sep=",")
emp2
#각 부서별 사원빈도 
table(emp2$V8)
#최대값, 최소값
table(emp2$V6)
max(emp2$V6)
min(emp2$V6)
#한꺼번에 같이 출력해주는 함수 fa

fa<- function(){
  a<- table(emp2$V6)
  cat("급여에 대한 빈도분석 결과 \n")
  print(a)
  cat("MAX = ", max(a), "\n")
  cat("MAX = ", min(a), "\n")
}

fa()

?function

hap <- function(x){
  i <- 0
  k <- 0
  while(i<x){i <- i+1 
     k <- k+i 
  }
  print(k)
}


hap(100)


hap <- function(n){
  s <- sum(c(1:n))
  cat("1부터",n,"까지의 합은",s,"입니다")
}


c(1:10)
c(10:1)

fac <- function(n){
  k <- 1
  for(i in c(n:1)){
    k <- k*i
  }
  print(k)
}

fac(5)

factorial(5)

#피타고라스 정리
#직각 삼각형의 각변의 제곱은 대각선의 제곱의 합과 같다. 

pytha <- function(n,m){
   x <- n^2 + m^2
   print(sqrt(x))
}

pytha(3,4)


#리턴 값이 있는 함수 
f3 <- function(x,y){
  add<- x+y
  return(add)
  cat("값 리턴함")
}

f3(100,200)

# 통계량을 구하는 함수

stat <- function(FUNC, data){
  switch (FUNC,
          SUM = sum(data),
          AVG = mean(data),
          VAR = var(data)
  )
}

data<-c(1:10)
stat('SUM',data)
stat('AVG',data)
stat('VAR',data)

n1 <- c(10,20,30,50,100,NA)
mean(n1, na.rm = T)
#NA여부를 상관없이 평균을 구해주는 mean2 

mean2 <- function(s){
   m<- mean(s,na.rm= T)
   cat("평균값", round(m,2))
}

mean2(n1)


# R 내장함수 
c(10,20,30)
seq(-2,2,0.2)
rep(1:3,3)
vec <- c(1:10)
vec
min(vec)
max(vec)
mean(n1,na.rm =T)
sum(n1,na.rm=T)

rnorm(20, mean=0,sd=1)
# 평균 0 표준편차 1 인 정규분포를 따르는 20개 데이터 생성 

runif(20,min=0,max=100)
#랜덤값 0~100에서 20개 소수
round(runif(20,min=0,max=100),0)
#난수
sample(1:200,20)
range(vec)


median(vec)
#데이터의 곱 
prod(vec) # vec : 1,2,3,4,5,6,7,9 전부 곱함
factorial(10)

abs(-5)
sd(rnorm(10,mean=0,sd=1))
sqrt(16)
table(vec) #빈도구하기 
log(10) #10의 자연로그 (밑수가 e )

# excel.csv 파일 읽어오기

excel <- read.csv(file= "excel.csv", header = T)
excel
str(excel)
head(excel,10)

colMeans(excel[1:5])
rowMeans(excel[1:5])
summary(excel) #요약통계량 = 기술통계량 
#반올림 함수
x <- c(1.5,2.5,-1.3,2.3)
x
round(mean(x),0)
ceiling(mean(x)) # x보다 큰 정수 
floor(mean(x))#작은 정수 
#난수 생성

#정규분포를 따르는 난수 생성
#형식) rnorm(n,mean=0,sd=1)
r<- rnorm(1000,mean=0,sd=1)
r
hist(r)

#균등 분포를 따르는 난수 생성
runif(n,min,max)
r2 <- runif(1000,min=0,max=1)
r2
hist(r2)

#3.이항분포를 따르는 난수 생성
#rbinom(n,sample size,prop)
#sample size를 대상으로 나올 수 있는 확률값 지정

n<-10
r3 <- rbinom(n,1,0.5)
r3

r4<- rbinom(n,1,0.25)
r4


r5 <-rbinom(n,3,0.5)
r5
