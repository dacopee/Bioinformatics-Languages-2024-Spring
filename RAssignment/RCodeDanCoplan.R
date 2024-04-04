#full path is C:\RIT Classes\BIO 230 Bioinformatic Lang\RCode
library(ggplot2)

print ("Hello, Welcome to Dan's R Code")

data <- read.table('gc_results.csv', header = TRUE, sep = ',')
#View(data)
results <- list()

for (col_name in names(data)) {
  anova_result <- aov(data[[col_name]] ~ 1)  # Perform ANOVA
  results[[col_name]] <- summary(anova_result)  # Store ANOVA results
}

# Print ANOVA results
for (col_name in names(results)) {
  cat("ANOVA for", col_name, ":\n")
  print(results[[col_name]])
  cat("\n")
}
