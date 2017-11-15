
dataset = read.csv('regression.csv', header = TRUE)
summary(dataset)

plot(dataset, pch = 16)


# Create a linear regression model
model = lm(formula = 'Y ~ X', data = dataset)

# Make a prediction for each X
y_pred = predict(model, dataset)

points(dataset$X, y_pred, col = 'blue', pch=4)

# let's find out how good is our prediction using linear regression
# we will use Root Mean Square Error 

rmse = function(error){
  sqrt(mean(error^2))
}

error = model$residuals # same as dataset$Y - y_pred
pred_rmse = rmse(error = error)

# now we know that our RMMSE of our linear regression model is 5.7.
# Let's try to improve is by SVR

library(e1071)
svr_model = svm(Y ~ X, dataset)

y_pred = predict(svr_model, dataset)
points(dataset$X, y_pred, col = 'red', pch=4)

error = dataset$Y - y_pred
pred_rmse = rmse(error = error) # 3.157066


tuneResult = tune(svm, Y ~ X, data = dataset, ranges = list(epsilon = seq(0,1,0.1), cost = 2^2:9))
print(tuneResult)

# Draw the Tuning graph
plot(tuneResult)


tuneResult = tune(svm, Y ~ X, data = dataset, ranges = list(epsilon = seq(0,0.2,0.01), cost = 2^2:9))
print(tuneResult)

# Draw the Tuning graph
plot(tuneResult)

tunedModel = tuneResult$best.model
tuned_y_Pred = predict(tunedModel, data = dataset)

error = dataset$Y - tuned_y_Pred
tuned_pred_rmse =  rmse(error = error) # 2.046548
