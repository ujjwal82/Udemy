# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Since we have less number of data we won't have split

# Fitting Linear Regression to the dataset

# lin_reg = lm(formula = Salary ~ Level, data = dataset)
# or 
lin_reg = lm(formula = Salary ~ ., data = dataset)


# Fitting Polynomial Regression to the dataset
dataset$Level2 = dataset$Level ^ 2
dataset$Level3 = dataset$Level ^ 3
dataset$Level4 = dataset$Level ^ 4
dataset$Level5 = dataset$Level ^ 5

poly_reg = lm(formula = Salary ~ .
              , data = dataset)

library(ggplot2)

# Visualizing Linear Regression results
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)), colour = 'blue') +
  ggtitle('Truth vs Bluff (Linear Regression)') +
  xlab('Levels') +
  ylab('Salary')


# Visualizing Polynomial Regression results
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)), colour = 'blue') +
  ggtitle('Truth vs Bluff (Polynomial Regression)') +
  xlab('Levels') +
  ylab('Salary')

# Visualizing Regression Model results for higer resolution and smoother curve.
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)

ggplot()+
  geom_point(aes(x = x_grid, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(poly_reg, newdata = data.frame(levels = x_grid))), colour = 'blue') +
  ggtitle('Truth vs Bluff (Regression Model)') +
  xlab('Levels') +
  ylab('Salary')



# Predict a new result with Linear Regression
y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))


# Predict a new result with Polynomial Regression
y_pred = predict(poly_reg, newdata = data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4 = 6.5^4, Level5 = 6.5^5))


