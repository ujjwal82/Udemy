x=c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
y=c(3,4,5,4,8,10,10,11,14,20,23,24,32,34,35,37,42,48,53,60)

#Create a data frame of the data
train=data.frame(x,y)


# Let's see how our data looks like. For this we use the plot function

#Plot the dataset
plot(train,pch=16)

# Linear regression
model = lm(y ~ x, train)

abline(model)

library(e1071)

# fit a SVM model
model_svm <- svm(y ~ x, train )

# use the prediction on the data
pred <- predict(model_svm, newdata = train)

# Plot the predictions and see our model
points(train$x, pred, col="blue", pch=4)

# Let's calculate RMSE (Root mean Square Error) for both the models

error <- model$residuals
lm_errors <- sqrt(mean(error^2)) # 3.832

# For svm we have to manually calulate the difference between actual values(train$y) with our predictions(pred)

error_2 <- train$y - pred
svm_error <- sqrt(mean(error_2 ^ 2)) # 2.696


# In this case the Linear model ahs RMSE of ~3.832 and SVM has the same of ~2.696, so this is clear that the SVM has accuracy higher than the linear regression. 
# We can further improve our SVM model and tune it so that the error is even lower.

svm_tune <- tune(svm, y ~ x, data = train,
                 ranges = list(epsilon = seq(0,1,0.1), cost= 2 ^(2:9))
                 )


# The best.performance denotes MSE.
sqrt(svm_tune$best.performance)

# Let's extract the best model 

# Best model
best_model_svm <- svm_tune$best.model
best_model_pred <- predict(best_model_svm, train)

# Let's find out the RMSE for the best model

best_model_error <- train$y - best_model_pred
best_model_rmse <- sqrt(mean(best_model_error ^ 2)) # 1.159

plot(svm_tune)

plot(train, pch=16)
points(x = train$x, y = best_model_pred, col="blue", pch=4)
