다음 client dataFrame 을 대상으로 조건에 맞게 처리하세요 

name<-c("aaa","bbb","ccc","ddd")
gender<-c("F","M","M","F")
price<-c(72,54,65,23)

client<-data.frame(name, gender, price)

1. price가 65만원인 고객은 "BEST" 미만인 고객은 "NORMAL" 문자열을 result에 넣고 client의 객체에 컬럼을 추가 


client$result <- ifelse(client$price>=65,"BEST","NORMAL")
client

2. gender가 M이면 "Male", "F"면 "Female" 형식으로 client의 객체에 gender2 컬럼을 추가하고 빈도수 구하기 

client$gender2 <- ifelse(client$gender =="M","Male","Female")
client

table(client$gender2)


3. 
다음 벡터(EMP)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
이 벡터 데이터를 이용하여 다음과 같은 출력결과가 나타나도록 함수를 정의하시오. 

# <Vector 준비>
EMP <- c("2014홍길동220", "2002이순신300", "2010유관순260")
library(stringr)

# <출력 결과>
# 전체 급여 평균 : 260

emp_year <-as.numeric(str_split_fixed(EMP,"[가-힣]{3}",2)[,1])
emp_pay<- as.numeric(str_split_fixed(EMP,"[가-힣]{3}",2)[,2])
emp_name <- str_extract(EMP,"[가-힣]{3}")
emp_avgpay <- mean(as.numeric(emp_pay))

emp <-data.frame(emp_name,emp_pay,emp_year)
emp

# 평균 이상 급여 수령자

# 이순신 => 300 

# 유관순 => 260 

#힌트) 사용 함수
#stringr 패키지 : str_extract(), str_replace()함수
#숫자변환 함수 : as.numeric()함수
#한글 문자 인식 정규표현식 : [가-히]  

# 함수 정의 : for()함수 이용 예  
emp_pay<-function(EMP){
  emp_year <-as.numeric(str_split_fixed(EMP,"[가-힣]{3}",2)[,1])
  emp_pay<- as.numeric(str_split_fixed(EMP,"[가-힣]{3}",2)[,2])
  emp_name <- str_extract(EMP,"[가-힣]{3}")
  emp_avgpay <- mean(as.numeric(emp_pay))
  
  emp <-data.frame(emp_name,emp_pay,emp_year)
  emp
  
  
  
  mean<-mean(emp$emp_pay)
  cat("전체 급여 평균 : ", mean,"\n")
  avghigh<-emp %>% filter(emp_pay<=mean) %>% select(emp_name,emp_pay)
  cat("평균보다높은사람 : ",as.character(avghigh[1,1]),avghigh[1,2],as.character(avghigh[2,1]),avghigh[2,2])

  
  cat("전체 급여 평균 :",mean(temp$sal),"\n")
  cat("평균 이상 급여 수령자 \n")
  for (i in c(1:nrow(temp2))){
    cat(as.character(temp2[i,'name']), "=>", temp2[i,'sal'], "\n")
  
  
  }
emp_pay(emp)

4. 함수 호출 


emp_pay(EMP)


5. RSADBE 패키지에서 제공되는 Bug_Metrics_Software 데이터 셋을 
대상으로 소프트웨어 발표 후 행 단위 합계와 열 단위 평균을 구하고,
칼럼 단위로 요약통계량을 구하시오.  



install.packages('RSADBE')
library('RSADBE')
data("Bug_Metrics_Software")
str(Bug_Metrics_Software)
Bug_Metrics_Software

colMeans(Bug_Metrics_Software)
a = Bug_Metrics_Software[,,2]
a
apply(a, 2, sum)
apply(a, 1, mean)
summary(a)