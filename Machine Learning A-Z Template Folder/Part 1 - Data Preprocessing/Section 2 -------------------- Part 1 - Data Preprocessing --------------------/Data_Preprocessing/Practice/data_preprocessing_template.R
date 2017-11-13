
dataset = read.csv('Data.csv');
dataset = dataset[,1:4]

# Splitting the dataset into train set and test set
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio=0.8)

training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling
# we need to scale only age and salary column, 
#   skip the country and Purchased columns
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])


