url <- "https://openapi.naver.com/v1/search/local.xml?"

searchString <- "query=종로3가맛집"]


# UTF-8 인코딩
searchString<- iconv(searchString,to ="UTF-8")
searchString<- URLencode(searchString)
searchString

etcString <- "&display=30&start=1&sort=sim"

url2 <- paste(url,searchString,etcString,sep= "")
url2

#clientID
clientId <- "8WV5lNCZj94ZpxlZ_Lps"
#client secret
clientSecret <- "VD5nxtqYD5"

library(httr)
result <- GET(url2, add_headers("X-Naver-Client-Id"=clientId,"X-Naver-Client-Secret"=clientSecret))
str(result)
result$content
#실제 내용으로 보려면 rawToChar 함수를 이용해서 변경

result2 <- rawToChar(result$content)
result2
#인코딩 필요

Encoding(result2) <- "UTF-8"
result2

#--------------------------------------------------------
#문자열 조작 

# ABC 를 ***로 변환
gsub("ABC","***","ABCabcABC")
#대소문자를 무시하고 변환
gsub("ABC","***","ABCabcABC",ignore.case = T)


#벡터 문자열 치환
x <- c("ABCabcABC","abcABCabc")
x
gsub("ABC","***",x)

# gsub("정규표현식","치환문자",데이터)
#핸드폰전화번호 패턴 : 010-숫자4-숫자4
# 010-1234-5678 --> 010 - ****-****

gsub("010-[0-9]{4}-[0-9]{4}","010-****-****","010-1234-5678")


#
"i love banana"                     
gsub("b.n","***","i love banana")   # "." 한글자 

# b이후 문자가 0개이상 있고 a로 끝나는 패턴을 ***로 치환
gsub("b.*a","***","i love banana")  #  ".*" 0개이상 a로 끝나는 패턴 

#------------------------------------------------------------
result2
# xml 태그를 공란으로 치환
result3 <- gsub("<(\\/?)(\\w +)*([^<>]*)>"," ",result2)
result3

result3 <- gsub("[[:punct:]]"," ",result3)
result3

result3<- gsub("[a-z]"," ",result3,ignore.case = T)
result3

result3<- gsub("[0-9]"," ",result3)
result3


result3<- gsub(" +"," ",result3)
result3


서울특별시 문제 제거
result3<- gsub("서울특별시"," ",result3)
result3
#종로구 제거 
result3<- gsub("종로구"," ",result3)
result3
#공백제거 
result3<- gsub(" +"," ",result3)


#텍스트 마이닝 

install.packages("Sejong")
install.packages("hash")
install.packages("rJava")
install.packages("tau")
install.packages("RSQLite")
install.packages("devtools")
# install.packages("KoNLP")
# Korean Natural Language Processsing


#단어 추출 테스트 
library(KoNLP)

extractNoun("안녕하세요 오늘은 기분 좋은 하루입니다.")

#검색 문장 내 단어 추출 

nonus <- extractNoun(result3)
nonus

str(nonus)

#길이가 1인 문자는 제외 

nchar(nonus)
[nchar(nonus)>1]
nonus<- nonus[nchar(nonus)>1]


# 제외할 단어 정의
excluNouns <- c("가맛집","음식","오늘","으로","해서","정도","돈화문","수표")


#특정 단어를 제외 
nonus <- nonus[!nonus %in% excluNouns]


length(nonus)
table(nonus)


wordT<- sort(table(nouns),decreasing=T)
wordT

#-----------------------------------

w<- c("망고","수박","딸기","포도","포도","포도","딸기","바나나","고기","고기","고기","고기","비빔밥","고기","젤리",
      "푸딩","마카롱","티라미슈")
w

word <- table(w)
word
# worldcloud
install.packages("wordcloud2")
library(wordcloud2)

#워드 클라우드 그리기

wordcloud2(word, size=1, shape="diamond")




txt1 <- readLines("815.txt")


txt1<-unlist(extractNoun(txt1))
txt1
table(txt1)
wordcloud2(table(txt1))



txt2<-sapply(txt1,extractNoun,USE.NAMES =  F)
txt2
class(txt2)
#리스트 벡터로
txt3<- unlist(txt2)
txt3
class(txt3)
is.vector(txt3)

wordcloud2(table(txt3))

# wordcloud2(table(txt2),size =10 , shape="diamond")


#오라클에 연결하기 

sessionInfo()

Sys.getenv()
install.packages("RJDBC")
library(RJDBC)


#드라이버 클래스명과 driver위치를 지정 
#java JDBC 드라이버 필요 

# drv <- JDBC("jdbc드라이버명명", classPath= "경로")
drv <- JDBC("oracle.jdbc.driver.OracleDriver", classPath= "E:\\app\\user\\product\\11.2.0\\dbhome_1\\jdbc\\lib\\ojdbc6.jar")

url <- "jdbc:oracle:thin:@192.168.0.4:1521:orcl"  
username<-"scott"
password<-"tiger"


192.168.0.4

conn<-dbConnect(drv,url,username,password)
conn

dept<-dbReadTable(conn,"DEPT")
dept

# 다른 테이블 저장 
# dbWriteTable(conn,"테이블명",객체)
dbWriteTable(conn,"DEPT99",dept)
#db.csv
write.csv(x = dept,file="db.csv",fileEncoding = "UTF-8",row.names = F)


dept10<- dbGetQuery(conn,"select * from dept where deptno = 10")
dept10





conn<-dbConnect(drv,url,username,password)
conn

dept<-dbReadTable(conn,"EMP")
dept
dfxx <- dbGetQuery(conn,"select deptno,  job, AVG(SAL) as avg from emp group by deptno , job")

dbWriteTable(conn,"df11",dfxx) #테이블 만들어서 넣기 

write.csv(x = dfxx,file = "df.csv",fileEncoding = "UTF-8",row.names = T)


dbDisconnect(conn)


# 부서번호별 job별 평균급여를 구해 df: dataframe 객체를 생성
# 자신의 db에 dfxx라는 테이블 생성
# 로컬pc에 df.csv 파일 생성 
# 자원정리 


#Mysql 에 연결하기 

drv <- JDBC("com.mysql.jdbc.Driver","E:\\dev\\Rstudio\\mysql-connector-java-8.0.21.jar")

url <-"jdbc:mysql://192.168.0.68:3306/testdb"

username <-"scott"
password <-"tiger"

conn2<-dbConnect(drv,url,username,password)
conn2



