#esquisse::esquisser()

library(ggplot2)
library(ggThemeAssist)
ggplot(seals) +aes(x = long, y = delta_long) +
  geom_point(size = 1.2,aes(colour=delta_lat))+
 scale_x_continuous(trans = "reciprocal") +
 labs(title = "Data_let") +
 theme_gray()+scale_color_gradient(low = "blue",high = "red")

(-10+sqrt((10)**2-80))/4
year=2020
year+10==2030


library(ggplot2)
x=seq(0,2*pi,0.0002)
f=function(x){
  y=x^2 * log(x) * sin(x)
  return(y)
}
y=f(x)
x==y
a=data.frame(x,y)

ggplot(a) +
 aes(x,y) +
 geom_line(size = 1, aes(colour=y) )+
 theme_gra

y()+scale_color_gradient(low = "purple",high = "violet")



library(ggplot2)
library(patchwork)
p1 <- ggplot(mtcars)+geom_point(aes(mpg,disp))
p2 <- ggplot(mtcars)+geom_boxplot(aes(gear,disp,group=gear))
p3 <- ggplot(mtcars) + geom_smooth(aes(disp, qsec))
p4 <- ggplot(mtcars) + geom_bar(aes(carb))
p1 + p2 + p3 + p4
c(2,3)+c(1,2)

library(reshape2)
female=c(0.83,0.17)
male=c(0.74,0.26)
wash=c('wash','notwash')
factor(wash)
a=data.frame(female,male,wash)
df=melt(a)   

library(ggplot2)
type <- c('A','B','C','D','E','F','G')
nums <- c(10,23,8,33,12,40,60)
df <- data.frame(type = type, nums = nums)
#绘制条形图
label_value <- paste('(', round(df$nums/sum(df$nums) * 100, 1), '%)', sep = '')
p <- ggplot(data = df, mapping = aes(x = 'Content', y = nums, fill = type)) + geom_bar(stat = 'identity', position = 'stack')
label <- paste(df$type, label_value, sep = '')

p + coord_polar(theta = 'y') + labs(x = '', y = '', title = '') + 
  theme(axis.text = element_blank()) +
  theme(axis.ticks = element_blank()) + 
  theme(legend.position = "none") + 
  (aes(y = df$nums/2 + 
  c(0, cumsum(df$nums)[-length(df$nums)]), x = sum(df$nums)/150, label = label)) 

p+coord_polar(theta = 'y') + labs(x = '', y = '', title = '') + theme(axis.text = element_blank()) + theme(axis.ticks = element_blank()) + scale_fill_discrete(labels = label)

# x=10L
# typeof(x)

library(ggplot2)
female=c(0.84,0.16)
male=c(0.7,0.3)
wash=c('wash','notwash')
a=data.frame(female,male,wash)
a
ggplot(a)+geom_bar(x=wash,y=female,aes(female,wash))

d <- data.frame(name = c("Lea", "Tia", "Amy"), year = c(2009, 2012, 2015))
d[d$name == "Tia", 1]

library(multcomp)
library(tidyverse)
attach(cholesterol)
aggregate(response,by=list(trt),mean)
cholesterol%>%group_by(trt)%>%summarise(mean=mean(response))


data(litter,package = 'multcomp')
attach(litter)
table(dose)
as_tibble(gesttime)


x <- seq(0, 10, by = 0.1)
plot(x, type = "n", axes = F, ylim = c(0, 0.5), 
     xlim = c(0, 10), ylab = "", xlab = "")
df <- c(1:4, 6, 9)
for(k in df){
  lines(x, dchisq(x, df = k), 
        col = which(df == k) + 1, lwd = 2)
}
axis(1, col = "grey", cex.axis = 1)
axis(2, col = "grey", cex.axis = 1)
legend('topright', legend = paste0("k = ", df), 
       col = 1:length(df) + 1, text.font = 3, 
       bty = "n", cex = 1, lty = 1, lwd = 2)
chisq.test()

smokers <- matrix(c(42, 15, 40, 23), 
                  nrow = 2, ncol = 2, byrow = TRUE)
smokers

library(HH)
ancova(weight~gesttime+dose,litter)

library(MASS)
attach(UScereal)
head(UScereal)






install.packages('bibliometrix', dependencies=TRUE)

library(bibliometrix)
biblioshiny()
library(tidyverse)
df=as_tibble(mtcars)
df
df=df %>% select(1:11)
scale(df)
has_rownames()
dataa=mtcars
library("pheatmap")
pheatmap(scale(app[,2:10],center=F))

  
library(tidyverse)
allin <- read_delim("C:/Users/Zz/Desktop/allin.csv", 
                    "\t", escape_double = FALSE, trim_ws = TRUE)
library(hrbrthemes)
ggplot(allin) +
  geom_area(aes(x=year, y=`All MP`),fill="#699fb3", alpha=1) +
  geom_line(aes(x=year, y=`All MP`),color="#699fb3", size=2) +
  # geom_point(aes(x=year, y=`All MP`),size=3, color="#27AFD9") +
 
  # geom_point(aes(x=year, y=Chitosan),size=3, color="#69b3a2") +
  geom_area(aes(x=year, y=Chitosan),fill="#697ab3", alpha=1) +
  geom_line(aes(x=year, y=Chitosan),color="#697ab3", size=2) +
  geom_area(aes(x=year, y=Alginate),fill="#69b3a2", alpha=1) +
  geom_line(aes(x=year, y=Alginate),color="#69b3a2", size=2) +
  theme_ipsum() +
  ggtitle("Evolution of something")







library(esquisse)
esquisse::esquisser()

r1 = Country_Production[order(-Country_Production[,2]),]

# load the library
library(forcats)
#f68060
# Reorder following the value of another column:
MPC %>%
  mutate(Countries = fct_reorder(Countries , `Record Count`)) %>%
  ggplot( aes(Countries , `Record Count`)) +
  geom_bar(stat="identity", fill="#f68160", alpha=1, width=.8) +
  coord_flip() +
  xlab("") +
  theme_classic()+
  ggtitle('Top 15 most published countries/regions')



library(streamgraph)

# Create data:
data <- data.frame(
  year=rep(seq(1990,2016) , each=10),
  name=rep(letters[1:10] , 27),
  value=sample( seq(0,1,0.0001) , 270)
)

# Basic stream graph: just give the 3 arguments
pp <- streamgraph(data, key="name", value="value", date="year", height="300px", width="1000px")
pp 

library(tidyverse)
f2 <- y ~ x + I(x^2)
oil
p2 <- ggplot(oil, aes(Time, Water, color=Group)) + theme_bw()+
  ggtitle('nonlinear fit')+
  geom_smooth(method = c('loess'), se=FALSE, col = 'black', span=0.5) + ##不规则拟合
  geom_smooth(method = "lm", formula = y ~ poly(x,2),color='blue',size = 2,se = T)+  ##二次拟合
  stat_poly_eq(formula = f2,
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")),
               parse = TRUE,label.x.npc = "right", label.y.npc = "top",size = 3) +#添加注释文字
  theme(axis.title= element_text(color = 'black',size= 12,face = 'bold'),
        axis.text = element_text(color = 'black',size = 10,face = 'bold'),
        plot.title = element_text(hjust = 0.5,size = 20,color = 'blue'))




A1 <-c(12.32,12.4,12.6)
B1 <-c(11.81,11.96,11.67)
t.test(A1,B1)


