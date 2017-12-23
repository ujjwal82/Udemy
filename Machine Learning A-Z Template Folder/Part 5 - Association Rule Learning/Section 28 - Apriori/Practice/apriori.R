# Apriori

# install.packages('arules')
library(arules)

# Data Processing
dataset <- read.csv('Market_Basket_Optimisation.csv', header = FALSE)
dataset <- read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)

itemFrequencyPlot(x = dataset, topN=10)

# Training Apriori on dataset
rules <- apriori(data = dataset, parameter = list(supp=0.003, conf=0.8))
rules <- apriori(data = dataset, parameter = list(supp=0.003, conf=0.4))

rules <- apriori(data = dataset, parameter = list(supp=0.003, conf=0.2))
rules <- apriori(data = dataset, parameter = list(supp=0.004, conf=0.2))
# Visualising the results
#inspect(rules)

# list of top 10 rules 
inspect(sort(rules, by='lift')[1:10])

