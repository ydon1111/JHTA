library(ggplot2)


mpg <- as.data.frame(ggplot2::mpg)

str(mpg)
write.csv(mpg,file = 'C:/Users/user/notebook/mpg.csv',fileEncoding = 'UTF-8')
