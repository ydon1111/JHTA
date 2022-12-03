
# 영화진흥위원회 사이트에서 박스오피스 영화 정보를 가져오기
# 네이버에서 영화제목으로 별점 가져오기
# df
# 영화제목 별점, 매출액, 스크린수, 장르, 별점
# 상관관계
# 시각화
library(rvest)
library(httr)
library(xlsx)
library(dplyr)
url<-"https://movie.naver.com/movie/search/result.nhn?query="
movie<-read.csv("kobis1.csv", header = T, sep = ",")
movie
movie<-head(movie, 10)
txt<-NULL
rating<-NULL
genre<-NULL
for (i in movie$영화명) {
  movie_name<-paste0(url,URLencode(i))
  txt<-read_html(movie_name)
  rating[i]<-txt%>%html_node("#old_content > ul.search_list_1 > li:nth-child(1) > dl > dd.point > em.num")%>%html_text()
  genre[i]<-txt%>%html_node("#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dd:nth-child(3) > a:nth-child(1)")%>%html_text()
}


rating
movie

df<-cbind(movie[2],rating,movie[4],movie[7],genre)
colnames(df)<-c("영화제목", "별점", "스크린수", "매출액", "장르")

df
# 상관관계
library(stringr)
# df$별점<-str_replace_all(format(df$별점),",","")
df$매출액<-str_replace_all(format(df$매출액),",","")
df$스크린수<-str_replace_all(format(df$스크린수),",","")


df$별점<-as.numeric(format(df$별점))
df$매출액<-as.numeric(format(df$매출액))
df$스크린수<-as.numeric(format(df$스크린수))

cor(df[2:4])

# 시각화
library(corrgram)
corrgram(df[2:4], upper.panel=panel.conf)
library(PerformanceAnalytics)
chart.Correlation(df[2:4], pch="+")


