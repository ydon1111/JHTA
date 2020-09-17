#작업 위치 
getwd()
#setwd("경로")
#메모리 객체(변수)
#변수목록확인
ls()

ls.str()
rm(a)
rm(list =ls())
a<- 100
save(a,file="test.RData")
rm(list=ls())
load('test.RData')

# ------------------------------------------

#자료형
#숫자형, 문자형, 논리형

a <- 100
b <- '대한민국'
c <- TRUE

#자료형
mode(a)
mode(b)
mode(c)
#물리적 자료형 

#NA: 관측이 안된 값
#NAN: Not A Number
0/0
#Inf : 무한대
3/0
#자료형이 맞는지 여부 확인?
is.numeric(a)
is.character(b)
is.logical(c)


score <- c(85,95,NA,75,65)
score 
mean(score,na.rm =T) #na 제거 후 
sum(score,na.rm = T)
# T 변수 , TRUE : 예약어 

x <- c(10,20,30,'40')
x
is.numeric(x)
#형변환 
y <- as.numeric(x)
y
#요인형(factor)
#동일한 값을 범주로 갖는 vector 
gender <- c("M","F","M","F","M")
gender
mode(gender)
fgender <- as.factor(gender)
fgender
mode(fgender)
class(fgender)

Sys.Date()
Sys.time()
today <- '2020-10-01 09:00:00'
today
mode(today)

#format
ctoday <- strptime(today, '%Y-%m-$d %H:%M:%S')
ctoday

today2 <- as.Date(today)
today2



#------------------------------------------------------
#벡터
#c() , seq() , rep()

x <- c(2,4,6,8,10)
y <- c(1:10)
x
y

#교집합
intersect(x,y)
#합집합
union(x,y)
#차집합
setdiff(x,y)

#색인 이용해서 참조 
x 
# 6 출력 
x[3]
#2~4 출럭
x[2:4]
#길이
length(x)
#3번빼고 나머지
x[-3]
# 패키지를 설치 
#install.packages("패키지명")
install.packages("RSADBE")
#패키지를 로딩
library(RSADBE)
data("Severity_Counts") #RSADBE 패키지에서 제공되는 데이터 셋 가져오기 

str(Severity_Counts)
Severity_Counts
# --------------------------------------------------
#vector 동일 데이터 타입을 갖는 1차줜 배열 
#matrix 동일 데이터 타입을 갖는 2차원 배열 
#matrix() , rbind() , cbind()

m <- matrix(c(1:5))
m
m <- matrix(c(1:9), nrow =3)
m
#m1 은 1부터 10사이의 짝수만 
m1 <- seq(2,10,2)
m1

#m2 는 1부터 10사이의 홀수만
m2 <- seq(1,10,2)
m2
#m3 는 m1 과 m2 를 행기준 matrix
m3 <- rbind(m1,m2)
m3  
  

m4 <- cbind(m1,m2)
m4

#자료형과 객체 Type 보기 
mode(m3)
class(m3)

#데이터 접근 [행,열]
m3

m3[2,3]
m3[,3]
m3[,c(3,4)]
m3[c(1,2),c(3,4)]

#------------------------------------------------------

#1부터 25까지 5행5열 matrix
#행기준 
mx <- matrix(c(1:25),nrow=5, ncol=5,byrow=T)
mx

ncol(mx)
nrow(mx)
#열의 이름
?matrix
colnames(mx) <- c("1번","2번","3번","4번","5번")

#행의 이름
rownames(mx) <- c("user1","user2","user3","user4","user5")

mx

#3번 문항의 최대값
max(mx[,3])

#5번 문항의 평균값
mean(mx[,5])

#모든 문항의 평균값
# apply(mx,행/열 기준, 적용함수명)
apply(mx,2,mean)
apply(mx,1,mean)
#---------------------------------------------------

# array : 동일 데이터 타입을 갖는 다차원 배열 

d <- c(1:12) # 12개 요소를 갖는 벡터 객체
# array()
#arr<- array(d,c(행,열,면))

arr <- array(d,c(3,2,2)) #3차원

arr[,,2]

# 2행만 조회 

# 배열 자료형 과 자료 구조 
mode(arr) #자료형
class(arr) #구조 

#iris

data("iris3")
iris3
str(iris3)


#-------------------------------------------
#list : 서로 다른 데이터 구조 
# 1차원 리스트 
list <- list("lee","마피아",100,"hong","홍길동",90)
list 
#모든 타입을 우너소로 가질수 있다.

list[[1]]
list[1][1]

# list 구조 ==> vector 
vec_list <- unlist(list)
vec_list
# 1차원 리스트 : 2개 이상의 원소를 갖는 리스트 
num <- list(c(1:5), c(6:10))
num
num[[1]][1]
num[2]

#key = value 형식
num2 <- list(first = c(1:5), second=c(6:10))
num2 
num2$first
num2[[1]][1]

member <- list(name= "둘리",age=10,address ="서울")
member

member$name

member$age <- 1000000000000000000000000000000000000
member$age
member$hobby <- "호이!"
member$hobby
#원소 제거
#나이 삭제
member$age <- NULL
member$age

mode(member)
class(member)

length(member)

#list data  처리 함수
a <- list(c(1:5))
b <- list(6:10)
a
b
#c(a,b) 최대값
lapply (c(a,b), max) #list 로결과반환

sapply (c(a,b), max) #vector로 결과 반환환

#1부터 20 사이의 랜덤값 5개 출력
v<-sample(1:20,5)
v

li <-list(v)
li

#1부터 100 사이의 랜덤값 5개를 v2에 
#v,v2에 평균값을  list로 리턴
#v,v2에 합계를 vector 로 리턴

v2 <- list(sample(1:100,5))
v2

lapply (c(v,v2), mean)
sapply (c(v,v2), sum)

#다차원 리스트 
mlist <- list(c1=list(1,2,3), c2=list(10,20,30), c3=list(100,200,300))
mlist


#-------------------------------------
#Data Frame : 행과 열의 2차원 자료 구조 
#DB Table 구조
no <- c (1,2,3)
name <- c("둘리","철이","밍키")
pay <- c(100,200,300)
emp <- data.frame("번호"=no, "이름"=name,"급여"=pay)
emp
#matrix

m <- matrix(c(1,"둘리",100,2,"철이",200,3,"밍키",300),3,byrow=T)
m
memp<-data.frame(m)
memp

#텍스트 파일을 읽어서 data.frame 
temp <-read.table('table.txt',header= T, sep="\t")
temp
class(temp)

#csv 파일 (comma seperator value)
csvemp<-read.csv('emp2.csv', header=F)
csvemp
#empno , ename, job, magr, hiredate , sal, coom, deptno
colnames(csvemp) <- c("empno", "ename", "job", "mgr", "hiredate", "sal", "comm","deptno")
csvemp

name <-c("empno", "ename", "job", "mgr", "hiredate", "sal", "comm","deptno")
cemp <- read.csv('emp2.csv',header = F , col.names = name)
cemp

#서브셋 만들기 
x <- 1:5
y <- 6:10
df <- data.frame(x,y)
df

x1 <- subset(df, x>=3)
x1
class(x1)
#y 값이 8이상인 레코드만 모아서 df
y1 <- subset(df, y>=8)  #조건으로 뽑기 
y1
class(y1)


# cemp 에서 급여가 3000 이상인 사원들만 모아서 
# cemp2 data frame 만들기

cemp2 <- subset(cemp, sal >= 3000)
cemp2
#직접 변경가능 
cemp2 <- edit(cemp2)

edit(cemp2)

#comm이 na가 아닌 데이터만 subset으로 만들기 

nona_emp <- subset(cemp, !is.na(comm))
nona_emp

#급여가 3000 이상이고 comm 이 na가 이닌

emp <- subset(cemp ,sal>= 1000 & !is.na(comm))
emp

temp

# nona_emp, emp
# 두개의 프레임 연결 

join_emp <- data.frame(nona_emp,emp)
join_emp

height <- data.frame(id=c(1,2),h=c(180,175))

weight <- data.frame(id=c(1,2),w=c(80,75))

#merge 결합 
user <- merge(height, weight , by.x ="id", by.y="id")
user

movie <- read.csv('movie.csv',header = F)
movie


#문자열 처리 함수 , 정규표현식
#stringr 
install.packages("stringr")
library(stringr)
#형식 ) str_extract("문자열","정규표현식")
str_extract("abcd12aaa33","[0-9]{2}")
str_extract_all("abcd12aaa33","[0-9]{2}")
str_extract("abcd12aaa33","[a-z]{2}")
str_extract("abcd12aaa33","[a-zA-Z]{2}[0-9]{2}")
str_extract_all("abcd12aaa33","[a-zA-Z]{2}[0-9]{2}")

jumin <- "111111-1111118"

str_extract_all(jumin,"[0-9]{6}-[1,2,3,4][0-9]{6}")

#email 양식 검사
email <- "hong@gamil.com"
result <- str_extract_all(email,"[a-zA-Z0-9]{4,}@[a-zA-Z0-9]{3,}.[a-zA-z]{3,}")
result


msg <- "푸른하늘은하수999abcabc"
result <- str_extract_all(msg,"[가-힣]{7}")
result                
#한글빼고 나머지만 추출 
result2 <- str_extract_all(msg,"[^가-힣]{7}")
result2
#문자열 길이 구하기 
length(msg)
str_length(msg)
#문자열 위치 (index)
str_locate_all(msg,'b')
str_locate_all(msg,'abc')

#부분 문자열 
substr <- str_sub(msg,5,8)
substr
#문자열 교체
str2 <- "BTS,블랙핑크,초신성"
str_replace_all(str2,"초신성","엑소")


#문자열 분리
str3 <- str_split(str2,',')
str3
#문자열 결합
str4 <- c('bts','블랙핑크','엑소')
str4
str5 <- paste(str4,collapse = ",")
str5

jumin2 <- "111111-1111118"
jumin3 <- str_sub(jumin2,1,8)
jumin3
c(jumin3,"*****")
paste(c(jumin3,"******"),collapse = "")

#특정문자열 기준으로 양쪽 분리 
jumin_result <- str_split_fixed(jumin2,'-',2)
jumin_result
jumin_result[,1]
jumin_result[,2]
