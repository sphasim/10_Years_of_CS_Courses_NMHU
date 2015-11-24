setwd("/Users/sphasim/Desktop")
getwd()
list.files()
orgdata <- read.csv("5000m-olympics.csv")
head(orgdata)
time=orgdata$time 
head(time)

Timeminmin <- as.numeric(sapply(strsplit(as.character(time), ":"), "[",1))
Timeinsec <- as.numeric(sapply(strsplit(as.character(time), ":"), "[",2))
totaltime = (Timeminmin)+ (Timeinsec)/60
totaltime
datause=cbind(orgdata,totaltime)
head(datause)
datause

