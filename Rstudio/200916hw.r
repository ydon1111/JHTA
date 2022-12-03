
library(rJava)
library(xlsx)

1. 본문에서 작성한 movie변수를 다음과 같은 단계를 통해서
movie.csv 파일로 저장한 후 데이터프레임으로 가져오시오.

1-1)> 작업디렉토리를 확인 하고 
작업  디렉토리에 "movie.xlsx"로 저장

movie <- read.csv(file = "movie.csv")
movie
write.table(movie,"movie.xlsx")
dim(movie)


1-2) 파일을 movie데이터 프레임으로 가져와서 결과 확인

movie <- read.xlsx(file="movie.xlsx",sheetIndex = 1,encoding = "UTF-5")
movie
str(movie)


1-3)  movie데이트 셋 구조 보기 함수를 이용하여 관측치와 컬럼수 확인
dim(movie)

1-4) 상위 6개 관측치 보기
head(movie,6)



2. 
emp3.xls 파일을 읽어온다.
dataFrame을 만든다. (emp)
수학성적이 90점 이상인 사람의 위치를 알아온다.
해당위치의 행을 가져온다.
여러열중 name 열만 출력한다. 

emp <- read.xlsx(file = "emp3.xls",sheetIndex = 2,encoding ="UTF-8")
emp

which(emp$mat>=90)
emp[c(which(emp$mat>=90)),]
emp[c(which(emp$mat>=90)),1]


2-1. 총점(total), 평균(avg ) 파생변수 추가 
emp$total<-apply(emp[-1],1,sum)
emp$avg<-emp$total/3
2-2.  grade 성적 ABCDF 파생 추가
emp$grade <-ifelse(emp$avg>=90,"a",
       ifelse(emp$avg>=80,"b",
       ifelse(emp$avg>=70,"c",
       ifelse(emp$avg>=60,"d","f"))))

emp
2-3. 평균값으로  히스토그램 그리기 
hist(emp$avg)

3. 
	library("dplyr")
	head(emp)
	데이터를 확인 
3-1 emp데이터 프레임에 class 열을 추가하고 
	1부터 6까지의 값을 갖도록 만들어준다. 

emp$class
1 2 3 4 5 6  1 2 3 4 5 6   ...... 
emp$class <- c(1:6)
emp
3-2 . 1반 학생들의 데이터만 추출 

emp[which(emp$class==1),]

3-3. 4, 5, 6반 학생들의 데이터만 추출 
emp[which(emp$class==4 |emp$class==5 |emp$class==6),]

3-4. 3반만 빼고 데이터를 추출 
emp[which(emp$class!=3),]


3-5 수학점수가 50점 이하인 학생들만 빼고 추출 
emp[which(emp$mat <= 50),]

3-6 1반 수학점수 50점 이하인 학생들만 추출 
emp[which(emp$mat <= 50 & emp$class==1),]

3-7 영어 수학점수가 50점 이하인 학생들만 추출 

emp[which(emp$mat <= 50 & emp$eng <=50),]

3-8 2, 4, 6 반 학생들만 추출 
emp[which(emp$class==2 |emp$class==4 |emp$class==6),]

3-9. 3반학생들의 수학 총점과 평균? 
m<-emp[which(emp$class==3),4]
sum(m)
mean(m)


