# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('50_Startups.csv')


# Encoding categorical data
dataset$State = factor(dataset$State,
                         levels = levels((dataset$State)),
                         labels = c(1:length(levels(dataset$State))))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting multiple regresson to the Training set
regressor = lm(formula = Profit ~ ., data = training_set)

#regressor = lm(formula = Profit ~ R.D.Spend, data = training_set)

# Predting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Building the optimal model using Backward Elemination
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State
               , data = dataset)

summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend
               , data = dataset)

summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend
               , data = dataset)

summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend
               , data = dataset)

sum_regressor = summary(regressor)
labels(sum_regressor$coefficients)


