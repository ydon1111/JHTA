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


plot ( pbinom(0:10, size = 10 , prob = 0.9),
       type = 'h',
       lwd = 10,
       main = '누적이항분포 10명중 7명 이상')




