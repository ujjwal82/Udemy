# Regression Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Since we have less number of data we won't have split


# Fitting Regression Model to the dataset
# Create your regressor here 

poly_reg = lm(formula = Salary ~ ., data = dataset)


# Predict a new result with Polynomial Regression
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))


# Visualizing Regression Model results
library(ggplot2)

ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), colour = 'blue') +
  ggtitle('Truth vs Bluff (Regression Model)') +
  xlab('Levels') +
  ylab('Salary')


# Visualizing Regression Model results for higer resolution and smoother curve.
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)

ggplot()+
  geom_point(aes(x = x_grid, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(levels = x_grid))), colour = 'blue') +
  ggtitle('Truth vs Bluff (Regression Model)') +
  xlab('Levels') +
  ylab('Salary')


