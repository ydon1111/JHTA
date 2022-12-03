# 다음값을 갖는 벡터를 출력하세요 
#  1. vector1 
#   1 ,3, 5, 7, 9 , ..., 99 

#  2. vector2 
#   1,1,1,2,2,2,3,3,3,4,4,4,5,5,5

#  3. R 문자가 5개 반복되는 vector3 
#    "R","R","R","R","R"

#  4. 1~10까지 3간격으로 연속된 정수를 갖는 vector4 
#   1 , 4 , 7 , 10 

# 5. 25~ -15까지 5간격으로 벡터생성 : seq()함수이용

# 6. 과일과 산지를 묶은 list 
# multi_fruit 
# 사과   대구 
# 오렌지 캘리포니아
# 딸기   논산 
# 망고   태국

#딸기 산지 출력

#망고 산지 출력

vector1 <- seq(1,100,2)
vector1

vector2 <- rep(1:5, each=3)
vector2 

vector3 <- rep("R",each =5)
vector3

vector4 <- seq(1,10,3)
vector4

vector5 <- seq(-15,25,5)
vector5

multi_fruit <- list("사과" = "대구","오렌지" = "캘리포니아", "딸기"="논산", "망고"="태국")

multi_fruit$딸기
multi_fruit[4]






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



9  최근 10일간 환율의 평균값 

날짜                  환율 
2020.09.14	1,184.00	
2020.09.11	1,187.00	
2020.09.10	1,186.90	
2020.09.09	1,187.50	
2020.09.08	1,189.00	
2020.09.07	1,188.00	
2020.09.04	1,189.50
2020.09.03	1,190.00	
2020.09.02	1,187.00	
2020.09.01	1,184.70	


date <- c("2020.09.14",
          "2020.09.11", 
          "2020.09.10",	
          "2020.09.09",		
          "2020.09.08",		
          "2020.09.07",	
          "2020.09.04",	
          "2020.09.03",		
          "2020.09.02",	
          "2020.09.01")
date
rate <- c(1184.00
            ,1187.00	
            ,1186.90	
            ,1187.50
            ,1189.00
            ,1188.00
            ,1189.50
            ,1190.00	
            ,1187.00	
            ,1184.70)
rate
rate
hw <- cbind(date,rate)
hw

apply(hw,1,mean)


matrix(1:2500, nrow =50, ncol = 50 , byrow = TRUE)


txtme <- read.table(file='./200914/me.txt',header = F,sep = "\t")
txtme

#자료에서 ' , ' 를 지워서 함
mean(txtme$V2)

#as.numeric(txtme$V2)
#rate <- as.numeric(txtme$V2)
#mean(rate)



12. 7번 문제의 자료 를 데이터 프레임으로 변환한다. 
data.frame(매트릭스)

name <- c("kim","lee","hong","choi")
kor <- c(80,50,100,85)
eng <- c(50,65,95,65)
sci <- c(70,90,35,80)
mat <- c(100,80,25,90)


score <-data.frame(NAME=name,KOR=kor,ENG=eng,SCI=sci,MAT=mat)
score



13. 총점을 구해 새로운 벡터로 만든다. 


score$TOTAL <- c(sum(score[1,-1]),sum(score[2,-1]),sum(score[3,-1]),sum(score[4,-1]))
score

14. 평균을 구해 새로운 벡터로 만든다. 

score$MEAN <- score$TOTAL/4
score

15. 기존에 데이터 프레임에 총점과 평균을 추가 한다. (열추가 ) 



