


# library(ggplot2)


#정규분포 그리기 

x <- seq(-5,5,length = 101)
x
y <- (1/sqrt(2*pi))*exp(-x^2/2)
#확률 밀도함수 구하는 방법
y
plot(x,y,type = 'l',col='red')


y1 <- dnorm(x, mean = 0,sd=1)
#정규분포 구하는 함수 
y1

abline(v = 0, col='blue')

#표준편차의 값이 다를때 모양 

y2 <- dnorm(x,mean =0 ,sd = 10)
y2

plot(x,y2,type ='l',com= 'red')


# Xnorm() 
# rnorm() 난수함수 : 랜덤하게 정규분포값 생성 


rnorm(5) 
# 평균이 100, 표준편차 5인 랜덤값 10개 

rnorm(10,mean =100,sd = 5)

# 확률밀도함수 

dnorm : 함수값 

dnorm(0,sd = 10)


pnorm(1) # x값 1을 기준으로 이하 확률 
pnorm(1, lower.tail = F)



x<-rnorm(100,mean=80,sd=7)
x
x <- sort(x)
y <- dnorm(x,mean = 80 ,sd = 7)
y
plot(x,y, type ='l',col='red')
abline(v = 80 , col ='blue',lty =3)


pnorm(92,mean =80,sd=7,lower.tail = F)

abline(v = 92 , col ='green',lty =3)


qnorm(0.95,mean = 80 ,sd=7, lower.tail = T)




x<-rnorm(100,60,30)
x
x <- sort(x)
y <- dnorm(x,60 ,30)
y
plot(x,y,type='l',col='red')
abline(v = 60 , col ='blue')



