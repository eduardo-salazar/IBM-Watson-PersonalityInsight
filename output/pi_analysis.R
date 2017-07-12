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


# check tweets of category grater than 1000 - 5000 
# Taking a sample of 10 users from 500 
min(pi[pi$tweets_cat == 5000,2])
max(pi[pi$tweets_cat == 5000,2])
sample_rows1 <- nrow(pi[pi$tweets_cat == 5000,])
pi[sample(sample_rows1,10),]
# user tweets  openness conscientiousness extraversion agreeableness neuroticism
# <dbl>  <int>     <dbl>             <dbl>        <dbl>         <dbl>       <dbl>
# 1   103833650   1902 0.8079038        0.26321551   0.63453321    0.19166221  0.05112899
# 2   177410033   3438 0.9183082        0.01548855   0.11344691    0.01168388  0.47053890
# 3   142991611   1444 0.1180202        0.15380177   0.01675244    0.23266870  0.09049763
# 4  1358241590   1790 0.4844187        0.43007354   0.83682434    0.72923936  0.36859863
# 5  2419614498   1058 0.3266841        0.02280085   0.25728388    0.81864486  0.03150605
# 6    39635037   1120 0.4628372        0.55134921   0.82479708    0.71355932  0.16733142
# 7   198753021   1733 0.1683145        0.13598137   0.46306556    0.45474153  0.15672073
# 8   566569669   1177 0.3155791        0.02368594   0.24723825    0.37986284  0.02268326
# 9    35086484   1967 0.2344686        0.26654767   0.47883041    0.29881123  0.13777676
# 10  121497721   2439 0.8598601        0.06332077   0.30710687    0.05136054  0.66747108

# Sample for range of 5003 - 9853
min(pi[pi$tweets_cat == 10000,2])
max(pi[pi$tweets_cat == 10000,2])
sample_rows2 <- nrow(pi[pi$tweets_cat == 10000,])
pi[sample(sample_rows2,10),]
# user tweets  openness conscientiousness extraversion agreeableness neuroticism
# <dbl>  <int>     <dbl>             <dbl>        <dbl>         <dbl>       <dbl>
# 1    91316071  11107 0.2987799         0.9591338   0.56690971     0.5214348  0.87170754
# 2  2425835000   7067 0.2490304         0.2465367   0.33072509     0.3496154  0.15326452
# 3  1899882806   6171 0.4866053         0.4235038   0.63951190     0.4717647  0.04919429
# 4    15519381   9011 0.4607482         0.3396960   0.59207634     0.2911924  0.65587154
# 5    24761830   7378 0.8761984         0.1068932   0.01278244     0.4467429  0.11683570
# 6   870560696  17247 0.8653035         0.2645292   0.38992036     0.2837453  0.18750608
# 7    64928068  16219 0.9672410         0.2347375   0.03886254     0.2806981  0.21644030
# 8  1957224986  11829 0.6430686         0.2613724   0.37118486     0.2575303  0.07938283
# 9  1408327218   5939 0.4411173         0.6046723   0.40713525     0.1484436  0.55840171
# 10 1230267290  12215 0.5929190         0.3490067   0.76854070     0.5204606  0.27748084

