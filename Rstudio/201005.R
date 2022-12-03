# y = ax + b 

# 선형회귀분석

# 변수 모델링 : y = ax1 +bx2 +....+ c 
# 회귀모델 생성
# 잔차(오차)분석 

# 독립성과 등분산성 검정 
# 정규성 검정 
# 다중 공선성 검사 
# 지나치게 연관성이 큰 변수는 제거 



data(iris)
# 꽃잎의 각 부분의 너비와 길이 등을 측정한 데이터 150 , 꽃 종류 

names(iris)
# Sepal.Length : 꽃받침의 길이
# Sepal.Width : 꽃받침의 너비
# Petal.Length: 꽃잎의 길이
# Petal.Width : 꽃잎의 너비
# Species : 꽃의 종류 

str(iris)

# 꽃받침의 길이 = 꽃받침의 너비, 꽃잎의 길이, 꽃잎의 너비 

formula = Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width
formula

model <- lm(formula = formula , data=iris)
model

summary(model)

# 등분산성 검정 

install.packages("lmtest")
library(lmtest)

# Durbin-Watson test 
dwtest(model)

# DW = 2.0604, p-value = 0.6013

# 보통 최소제곱 (ordinary least sqares)으로 계산된 잔차를 이용하는 선형모델에서
# 오차항의 계열 상관을 검정하는것 

# d --> 2 에 가까우면 오차항들은 서로 독립
# 0: 양의 상관관계
# 4: 음의 상관관계계

# 귀무가설 : 자기상관 <= 0 
# 대립가설 : 자기상관 > 0

# 잔차 정규성 검정
attributes(model)
# coefficients : 상관계수
# residuals : 잔차
# fitted.values : 적합값

res = resid(model)
res

# 잔차의 정규분포
# 귀무가설 : 정규분포와 차이가 없다. 
# 대립가설 : 정규분포와 차이가 있다. 
# 표본 개수 : 30개 


shapiro.test(res)
# W = 0.99559, p-value = 0.9349
# 귀무가설 채택 
# 잔차는 정규분포를 따른다고 할 수 있다. 

# 다중공선성 검사
# 독립변수에 강한 상관관계로 인해서 회귀분석의 결과를 신뢰 할 수 없는 현상 

# ex : (섭씨온도, 화씨온도) , (생년원일 , 나이) 

# 해결방법 : 강한 상관관계를 갖는 독립변수를 제거 

# 분산 팽창 인수 : vif(Vriance inflation Factor)
install.packages("lmtest")
library(car)
library(lmtest)

vif(model)
# 10이상인것은 다중공선성 문제 의심 

cor(iris[,-5])


# 0.9628654 : Petal.Length , Petal.Width 

formula <- Sepal.Length ~ Sepal.Width + Petal.Length 
model <- lm(formula = formula,data = iris)
model
summary(model)

# p-value: < 2.2e-16
# 공식
# Sepal.Length = 0.59552*Sepal.Width + 0.47192 * Petal.Length +2.24914

# iris data 중에서 train : 70% , test 30% 
# 1.전체 데이터 150개중 : 70만 랜덤하게 번호를 뽑는다.
nrow(iris)
t<-sample(1:nrow(iris),nrow(iris)*0.7)
t
# 2.이 번호에 해당하는 관측치만 train 변수에 담는다. 

train <- iris[t,] 
nrow(train) : 105

# 3. 나머지 30%만 test변수에 담기
test <-iris[-t,]
test
nrow(test)

# 분석
result.lm <- lm(formula = formula,data=train)
summary(result.lm)


# y = ax1 + bx2 +c

# 회귀분석 결과를 대상으로 회귀방정식을 적용한 새로운 값 예측 

result2 <- predict(result.lm,test)
result2
length(result2)
head(test)
head(result2)
test$result2 <- result2
test[,c("Sepal.Length","result2")]

data <- read.csv("product_sales.csv",header = T )
data

nrow(data)
str(data)
# 총구매금액, 구매횟수, 평균구매액, 방문횟수
# 상품 구매 금액 예측 


# 종속변수 : 총구매금액 
# 독립변수 : 구매횟수 , 평균구매액 , 방문횟수 

# train : 7 , test : 3 

t <- sample(1:nrow(data),nrow(data)*0.7)
t

train <- data[t,] 
train

test<-data[-t,]
test

formula <- tot_price ~ buy_count + visit_count + avg_price 
model <- lm(formula = formula , data = train)
model

summary(model)
# 식으로 표현하기 
# y = ax1 + bx2 + cx3 + d 
# tot_price = 0.41413*buy_count + -0.61303*visit_count + 0.71040*avg_price 
              # +2.67052

# 잔차 등분산? 정규성?
library(lmtest)
library(car)
# durbin-watson test
dwtest(model)
# 귀무가설 채택 : 자기상관 관계가 없다. 

res <- resid(model)
shapiro.test(res)
# data:  res
# W = 0.98994, p-value = 0.6263
# 귀무가설 : 정규분포와 차이가 없다.
# 대립가설 : 정규분포와 차이가 있다. 

# Shapiro_Wilk normality test 


vif(model)
# 다중공선성?
cor(data[,-1])

# 0.9627571 : visit_count , avg_price 


result3 <- lm(formula = tot_price ~ buy_count + avg_price, data = train)
summary(result3)
# y = 0.38642*buy_count + 0.45669*avg_price + 2.96926

pred <- predict(result3, test)
pred

test$pred <- pred 
head(test[,c("tot_price","pred")],5)


#shiny 패키지 설치
install.packages("shiny")
library(shiny)
runExample()
runExample("01_hello")
runExample("02_text")
