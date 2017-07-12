#Install Packaged
install.packages("readr")
install.packages('plyr')
install.packages('dplyr')

#Import Packaged
library(readr)
library(ggplot2)
library(plyr)
library(dplyr)
# Import file
pi <- read_csv("/Users/eduardosalazar/Documents/apps/watson/output/pi_target_user.csv")

# Analysis of PI target Users
#box plot
x <- c("Openees","Conscientiousness","Extraversion","Agreeableness","Neuroticism")
mean <- sapply(pi[,c(3:7)],mean)
median <- sapply(pi[,c(3:7)],median)
stdev <- sapply(pi[,c(3:7)],sd)

data_plot <- data.frame(trait=x,mean=mean,median=median,stdev=stdev)
ggplot(data_plot,aes(trait,mean,fill=trait)) +
  geom_bar(colour="black",stat="identity") +
  guides(fill=FALSE) +
  geom_errorbar(aes(ymin=mean-stdev, ymax=mean+stdev),
                width=.2,                    # Width of the error bars
                position=position_dodge(.9))

#histogram - frequency of tweets
hist(pi$tweets_cat)
pi$tweets_cat <- cut(pi$tweets, seq(0,50000,5000),labels=c(5000,10000,15000,20000,25000,30000,35000,40000,45000,50000))
ggplot(data.frame(pi), aes(x=tweets_cat)) +
  geom_bar()

result.tweets_by_group <- aggregate(rep(1, length(paste0(pi$tweets_cat))),
                             by=list(pi$tweets_cat), sum)
colnames(result.tweets_by_group) <- c("#tweets","count")
result.tweets_by_group


# check tweets of category grater than 5000 
# Taking a sample of 10 users from 500 
sample_rows1 <- nrow(pi[pi$tweets_cat == 5000,])
pi[sample(sample_rows1,10),]
# Sample for range of 10000 - 15000
sample_rows2 <- nrow(pi[pi$tweets_cat == 10000,])
pi[sample(sample_rows2,10),]


