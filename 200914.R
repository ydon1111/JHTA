1+1
#현재 작업디렉토리 확인 
getwd()



#변수 
a = 10 
a
b <- 20
b
30 -> c 
c


#combin 으로 묶음
x = c(10,20,30) 
x
mean(x)

mean(x=c(100,80,50))
mean(x <- c(50,100,90))

x <- 3
y <- 6
#사칙연산 가능

x+y 
x-Y
x*y
x/y

x^y
x**y

x <- 20
y <- 6

x%%y  # 2 20/6 ==> 나머지 2

x%/%y # 3 20/6 ==> 몫 3 

a
print(a)

dim(available.packages())

#session 보기 

sessionInfo()


# 변수명명법
# a ~ z , A~Z , 0~9 , _, . 
# 첫 글자는 알파벳 or . 으로 시작해야 한다.

# x9001_123.a
# Acs-2091  '-'  안됨
# .99accea3 


# integer : 100 ,200 ,3000 
# numeric 10.4 ,20.3
# NA(Not Available) : 데이터가 없음 
# NULL : null객체 , 변수가 초기화 되지 않음 


# 문자열
# 한 개 문자에 대한 데이터 타입 : char 

# 'big_data' , "big_Date2"


var1 <- 'big_data'
var2 <- 'big_data2'

var3 <- NA #데이터 없음
var3 
is.na(var3)

var3 <- NULL
var3 
is.null(var3) # null 이 맞는지 확인


x <- "hello R world"
x
y <- "hello R world"
y


# 스칼라 변수 
# 단일 값을 저장할 수 있는 변수 

#boolean 
# TRUE ,FALSE : 예약어 

TRUE 
FALSE 
T  # 전역변수
F  # 전역변수


#TRUE <- FALSE 

T <- FALSE 
T
T <- TRUE 


# 1. var1 변수에 100 , var2 변수에 8 
# var3변수에 TRUE를 대입하고 콘솔에 출력 
var1 <- 100
var2 <- 8
var3 <- T


# 2. var1 과 var2의 산술연산결과를 출력 

var1 + var2 
var1 - var2 
var1 * var2
var1 / var2

# 3. 홍길동의 국어 , 영어 , 수학 점수를 구해보자 
# 국어 : 80 , 영어 : 70 수학 :20

hong <- c(80,70,20)
names(hong) <- c("국어","영어","수학")


mean(hong)
sum(hong)
max(hong)
min(hong)
hong 

# 패키지 로딩 
# ggplot2 <-- 
install.packages("ggplot2")

available.packages()
# 세션상태
sessionInfo()
#패키지 로딩
library(ggplot2)
sessionInfo()

# 빈도 막대 그래프 출력 
qplot(hong)


# 범주형 데이터
# 데이터가 사전에 정해진 특정 유형으로만 분류 

# 명목형 
# 크기 비교가 불가능한것 

gender <- factor("m",c("m","f")) #명목형
gender 

size <- factor("s",c("s","m","l"),ordered=TRUE)
size 

# 팩터의 레벨 갯수
nlevels(gender)
nlevels(size)

#팩터인지 확인
is.factor(gender)
#의미? 순서형으로 변황
gender2 <- ordered(gender,levels=c("m","f"))
gender2

#Vector 
# 한가지 스칼라 데이터 타입으 데이터를 저장할 수있다.
# 다른 언어 배열의 개념 

# 생성함수 c(), seq(), req()
x <- c(1,2,3,4,5)
x
class(x)

# 3번째 데이터를 출력 

x[3] # [index] : 1부터 시작 
#컬럼의 이름

names(x) <- c("kim","lee","park","choi","hong")
x

# 3번만 빼고 나머지를 출력 
x[-3]

# for (i = ; i <= x.length; i++)

x[2:4]

#길이
length(x)
# 행또는 열의 수를 반환
NROW(x) # 대소문자 주의 

# 1부터 20까지의 값을 y변수에 할당 
# y 출럭 

y <- c(1:20)
y

# 1부터 20까지의 홀수는?
y2 <- seq(1,20,2)
y2

#반복해서 사용 
y3 <- rep(1:3,3)
y3

#각각 3번씩 반복 
j <- rep(1:10, each=3)
j

?rep


#shift + alt + 화살표 방향 아래키
x<-c(1,3,5)
y<-c(3,5,7)
x
y

#동일 객체인지 여부 

identical(x,y)
#교집합
intersect(x,y)
#합집합
union(x,y)
#차집합
setdiff(x,y)

#어벤져스반 학생들의 점수를 
#score 변수에 담는다.
#아이언맨 : 80
#헐크 : 30
#캡틴아 : 70
#토르 : 50

score <- c(80,30,70,50)
names(score) <-c("아이언맨","헐크","캡틴아","토르")
score

mean(score)
sum(score)
min(score)
max(score)


# x 변수에 1부터 100까지의 5의 배수 값을 담고
# x의 평균, 총점을 구한다 .

x <- seq(5,100,5)
x

mean(x)
sum(x)

intersect(score,x)

#연산자 
#value %in% x 

1 %in% c(1,2,3)

a <- c(1,2,3)
a
a+3 

v1 <- c(33,-5,20:33,12,-2:3)
v1 
v2 <- c("홍길동","이순신","유관순")
v2
v3 <- c(T,TRUE,FALSE,T,TRUE,F,T)
v3
#T, TRUE의 차이점?
#T는 전역변수 TRUE는 예약어 
v4 <- c(33,12,5,8,"4")
v4  #모두 문자로 읽어옴 
#sum(v4)
is.vector(v4)
class(v4)
#형변환
#is.XXX(변수) XXX자료형인지 여부 판단 
#as.자료형()
num <- as.numeric(v4)
num
class(num)
sum(num)


v5 <- c(10:15,"9",11:25)
# v5의 합계를 구하려고한다. 
sum(v5) # error

sum(as.numeric(v5))

#sample(데이터추출범위,데이터추출갯수,replace = FALSE)
#random하게 숫자 추출 
# replace = TRUE or FALSE  : 복원추출여부 확인

sample(1:10,5, replace = TRUE)  #복원 추출 


sample(1:45,6, replace = FALSE)
# 랜덤은 ... 로직에 의해서 만들어짐..

set.seed(1234) # 동일한 숫자로 나옴 , 로직의 주소 
sample(1:45,6, replace=FALSE)


#list 
#서로 다른 데이터 구조 
# (key,value) 형태의 데이터를 담는 연관 배열 

#python => dictionary

varList <- NULL
#1차원 리스트 

varList <- list("lee","이순신",c(95,100),"hong","홍길동",85)
varList

class(varList)

varList[3]
varList[2]

# 85를 출력

varList[6]

#key:value
num2 <- list(first =c(1:5),second=c(6:10))
num2
num2$first
num2[1]


member1 <- list(name="홍길동",age=20,addrs="한양",gender="남",htype="아파트")
member1 
class(member1)

member1$name
member1[3]

#list 에서 원소 접근 : 변수$키

# 홍길동의 나이를 25로 변경

member1$age <- 25
member1$age

member1

member1[1] <- "hong"
member1[1]

member1$id <-"aaa"
member1$pwd <-"1234"

member1$age <- NULL
member1 

member2 <- list(name="뽀로로",age=13 , addrs = "눈덮인숲속마을",htype="단독주택")
member2

#뽀로로 주소출력
member2$addrs
member2$age <- 20 
member2

member2$hobby <- "놀기"
member2$age <- NULL
member2


# matrix : 동일 데이터 타입을 갖는 2차원 배열

m1 <- matrix(c(1:5))
m1

m2 <- matrix(c(1:9), nrow=3)
m2

m3 <- matrix(c(1:9), nrow=3, byrow=TRUE) #좌측으로 변수 
m3

#1부터 25까지 5행5열짜리 matrix를 완성하세요

m4 <- matrix(c(1:25), nrow=5, byrow=TRUE)
m4

m5 <- matrix(seq(1,25), nrow=5)
m5


x1 <- c(5,40,50:52)
x1

x2 <- c(30,5,6:8)
x2

mr <- rbind(x1,x2)
mr

mc <- cbind(x1,x2)
mc
# 10 ~ 19 까지 10개의 데이터를 2개의 행으로 생성
# m3 

m3 <- matrix(c(10:19), nrow = 2, byrow=TRUE)
m3

m3 <- matrix(10:19 , 2)
m3
class(m3)


#벡터 4개를 만들고 함수를 사용해서 
#매트릭스를 생성하세요


v1 <- c(100,80,50)
v2 <- c(50,30,10)
v3 <- c(1,2,3)
v4 <- c(95,85,75)

mc <- cbind(v1,v2,v3,v4)
mr <- rbind(v1,v2,v3,v4)

mc
mr

r1 <- c(100,50,1,95)
r2 <- c(80,30,2,85)
r3 <- c(50,10,3,75)

mc <- cbind(r1,r2,r3)
mr <- rbind(r1,r2,r3)

mc
mr

mr[,2]
mr[2,]
mr[2,2]

#3맨배고

mr[-3,]

mr[c(2,3),c(1,2)]

m5 <- matrix(1:20, nrow=4,ncol=5, byrow=TRUE)
m5

?matrix
#byrow = T 행방향으로 배열
#byrow = F 열방향으로 배열 


mr
# 컬럼이름 부여하기 

colnames(mr) <- c("one","two","three")
mr
rownames(mr) <- c("p1","p2","p3","p4")
mr


# apply (변수,행/열 기준, 함수명)

apply(mr,1,max) # 1 행 기준으로 ,2 열 기준
apply(mr,2,max) # 1 행 기준으로 ,2 열 기준

#행단위 합계
apply(mr,1,sum)


k1 <- c(80,90,70,100)
k2 <- c(50,65,90,80)
k3 <- c(100,95,35,25)
k4 <- c(85,65,80,90)

mc <- rbind(k1,k2,k3,k4)
mc

colnames(mc) <- c("kor","eng","sci","mat")
rownames(mc) <- c("kim","lee","hong","choi")

mc

apply(mc,1,sum)
apply(mc,1,mean)
apply(mc,2,sum)
apply(mc,2,mean)


# array 
# array(데이터, dim= c(컬럼갯수,row갯수,3차원 갯수)
?array

a = array(c(1:12), dim=c(3,4,2))
a
a[3,2,1]
a[3,3,1]  #[행,열,면]


d <- c(1:20)
d
class(d)
arr <- array(d,c(4,5,2))
arr
arr[,,1]
# 1면 5열만 출력 
arr[,5,1]


#DataFrame 
#서로 다른 데이터 타입을 갖는 컬럼
#리스트 보다 더 활용범위가 넓다 
#dmbs의 테이블 구조 
#excel의 스프레드 시트 

no <-c(1,2,3)
name <- c("kim","lee","park")
pay <- c(150,250,300)
vemp <-data.frame(NO=no,NAME=name,PAY=pay)
vemp

#vemp2
#EMPNO       ENAME       SAL
#7369        SMITH       800
#7499        ALLEN      1600
#7521        WARD       1250

empno <- c(7369,7499,7521)
ename <- c("SMITH","ALLEN","WARD")
sal <- c(800,1600,1250)
vemp2 <- data.frame(EMPNO=empno,ENAME=ename,SAL= sal)
vemp2
vemp2$SAL
mean(vemp2$SAL)


name <- c("홍길동","이순신","유관순","둘리","고길동")
kor <- c(100,80,90,80,80)
mat <- c(20,70,80,50,90)

score <- data.frame(NAME=name,KOR=kor,MAT=mat)
score

mean(score$KOR)
mean(score$MAT)
min(score$MAT)


txtemp<- read.table(file='table.txt', header=T,sep="\t")
txtemp

#요스의 갯수 알아오기 
#vector 는 length()로
#matrix, dataframe은 dim()
dim(txtemp)

# 직원들의 월급 합계
sum(txtemp$SAL)
sum(txtemp[6])
# 급여 평균
mean(txtemp$SAL)
# 급여 최대값

nrow(txtemp)
ncol(txtemp)
names(txtemp)
head(txtemp)
tail(txtemp)
str(txtemp)

T <- TRUE
T
#도수 분포표 
table(txtemp)

