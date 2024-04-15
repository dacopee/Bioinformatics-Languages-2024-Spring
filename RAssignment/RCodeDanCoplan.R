library(ggplot2)

print ("Hello, Welcome to Dan's R Code")
setwd("C:\\RIT Classes\\BIO 230 Bioinformatic Lang\\RCode")

#read data
data <- read.table('gc_results.csv', header = TRUE, sep = ',')
#View(data)
str(data)

#make new stats to graph
avg_percentages <- aggregate(GC_Percentage ~ Chromosome, data = data, FUN = function(x) {
  c(avg = mean(x), sd = sd(x))  # Return named vector with avg and sd
})
avg_percentages$avg <- avg_percentages$GC_Percentage[, "avg"] # separates out the avg and sd columns for later refrence
avg_percentages$sd <- avg_percentages$GC_Percentage[, "sd"]

#ANOVA - analysis of variance (backwards)
oneway_result <- oneway.test (GC_Percentage ~ Chromosome, data, var.equal = TRUE)
print(oneway_result)

#print error bar plots
ggplot(avg_percentages, aes(x = Chromosome, y = avg)) +
  geom_bar(stat = "identity", fill = "skyblue", alpha = 0.7) +
  geom_errorbar(aes(ymin = avg - sd, ymax = avg + sd),width = 0.4) +
    labs(x = "Chromosome", y = "Average GC Percentage", title = "Error Bar Average GC Percentage by Chromosome with Error Bars") +
  theme_minimal()


