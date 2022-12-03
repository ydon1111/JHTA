#확률 분포 

#이항분포 


#확률밀도함수 : d~~
#누적분포함수(점수) : p~~
#누적분포함수(확률) : q~~~

#이항분포
#이항분포 확률밀도
#dbinom(성공횟수,size(시행횟수n),prob(성공확률))

#마트 할인쿠폰 성공사례
#시행횟수 :3명
#성공확률 : 90%
#p(x=a) 확률 계산


dbinom(0,size =3 , prob = 0.9)

dbinom(1,size =3 , prob = 0.9)

dbinom(2,size =3 , prob = 0.9)
dbinom(3,size =3 , prob = 0.9)


#이항분포 확률밀도 graph 

y<- dbinom(0:3, size = 3, prob =0.9)
y

plot(0:3, y, 
     type = 'h',
     lwd = 10 ,
     col ='red', 
     ylab ='확률',
     xlab = '성공확률 x ',
     main = '이항분포')


# 확률 질량함수 < ----- > 확률 밀도함수 
# 이산확률 변수에서 특정 값에 대한 확률을 나타내는 함수 

# 누적 확률 계산 
# P(x<=a) 이하 lower.tail = TRUE
# P(x <a ) 초과 lower.tail = FALSE
# P(x <= 1) 이하로 받을 확률 

pbinom(1, size = 3 , prob = 0.9 , lower.tail = TRUE)

# P(x >1 )초과로 받을 확률 

pbinom(0,size = 3 , prob = 0.9 , lower.tail = FALSE)

# 누적 이항분포 graph

plot (pbinom(0:3,size = 3 ,prob = 0.9),
             type = 'h',
             lwd =10,
             col ='red',
             main = '누적이항분포')


#문제
#10명중 7명 이상 : P(X> 6) 확률 0.9 계산 


plot (pbinom(6,size =10, prob = 0.9,lower.tail = FALSE),
      type = 'h',
      lwd =10,
      col ='green',
      ylab = '확률',
      xlab = '성공확률 x ',
      main ='이항분포 10명중 7명이상 ')


plot (0:10, (pbinom(0:10, size = 10 , prob = 0.9),
       type = 'h',
       lwd = 10,
       main = '누적이항분포 10명중 7명 이상')



#포아송 분포 (Poisson distribution )

확률질량함수
# dpois(발생건수 , lamda (단위시간당 평균 발생건수 ))

# 평균발생 건수 : 1.5 회
# P(X = a ): 확률계산

dpois( x= 0 , lambda = 1.5)

dpois( x= 1 , lambda = 1.5)


dpois( x= 0:5 , lambda = 1.5)

# 포아송 분포 확률질량 함수 그래프 

plot(dpois(x=c(0:10), lambda = 1.5),
      type='h',
      lwd = 10,
      col ='red',
      xlab = '성공확률 x ',
      main = '포아송분포')

# 포아송분포 누적확률

# 이하 P(X<=a)
# 2회 이상 받을 확률 P(X >1 )확률 계산
# 포아송분포 누적 확률 그래프 

plot(ppois(0:10,lambda =1.5,lower.tail = FALSE),
     type ='h',
     lwd = 10,
     col ='green',
     main = '누적 포아송분포포')

#1. p(X<=2)이하로 받을 확률 

plot(ppois(0:10,lambda=1.5,lower.tail = TRUE),
     type = 'h',
     lwd = 10,
     col = 'green',
     main ='맞나?')

#2. 어느 택배회사의 전화 상담실에는 1시간당 평균 240건의 전화 요청이 들어온다.
# 그럼 1분동안 걸려오는 전화요청이 2건 이하일 확률을 구하시오. 

ppois(2,lambda = 4 )

# 지수분포

# 지수분포 누적확률 계산 
# P(X <= a ) lower.tail = TRUE
# P(X <= a ) lower.tail = FALSE


pexp(q=대기시간,rate = '평균발생건수(λ)')
# 평균 발생건수 5분에 1.5회
# 단위시간 5분에 1.5회
# 대기시간 1분 : 0.2 
# ------------------------
# 단위시간 
# 1분 P(X <= 1/5) 이내로 받을 확률 

pexp(q=1/5 , rate = 1.5 , lower.tail = TRUE)


#지수분포 누적확률 그래프 
x <- seq(0,3,length = 500)

plot(x,dexp(x,1.5),
      type='l',
      ylim = c(0,1.5))
abline(v=0.2, col='red',lty =3 )




