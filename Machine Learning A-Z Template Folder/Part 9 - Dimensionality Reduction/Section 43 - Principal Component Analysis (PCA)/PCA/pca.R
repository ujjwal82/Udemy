# PCA

# Importing the dataset
dataset = read.csv('Wine.csv')
#dataset = dataset[1:13]

# Encoding the target feature as factor
# dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Customer_Segment, SplitRatio = 0.8)
training_set_pca = subset(dataset, split == TRUE)
test_set_pca = subset(dataset, split == FALSE)

# Feature Scaling
training_set_pca[-14] = scale(training_set_pca[-14])
test_set_pca[-14] = scale(test_set_pca[-14])

# Applying PCA
# install.packages('caret')
library(caret)
library(e1071)

pca = preProcess(training_set_pca[-14], method = 'pca', pcaComp = 2)
training_set = predict(pca, training_set_pca)
training_set = training_set[c(2,3,1)]
test_set = predict(pca, test_set_pca)
test_set = test_set[c(2, 3, 1)]

# Fitting SVM to the Training set
library(e1071)
classifier <- svm(formula = Customer_Segment ~ ., 
                  data = training_set,
                  type = 'C-classification',
                  kernel = 'linear')  # try diferent kernel for better performance

# Predicting the Test set results
# install.packages('rpart')
library(rpart)
prob_pred = predict(classifier, type = 'response',
                    newdata = test_set[-3])

# Making confusion matrix
cm = table(test_set[,3], prob_pred)

# Visualizing the Training set results
# install.packages('ElemStatLearn')
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('PC1', 'PC2')
y_grid = predict(classifier, type = 'response', newdata = grid_set)
plot(set[, -3],
     main = 'Support Vector Machine (Training set)',
     xlab = 'PC1', ylab = 'PC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 2, 'deepskyblue', ifelse(y_grid == 1, 'springgreen3', 'tomato')))
points(set, pch = 21, bg = ifelse(set[, 3] == 2, 'blue3',ifelse(set[, 3] == 1, 'green4', 'red3')))

# Visualizing the Test set results
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('PC1', 'PC2')
y_grid = predict(classifier, type = 'response', newdata = grid_set)
plot(set[, -3],
     main = 'Support Vector Machine (Test set)',
     xlab = 'PC1', ylab = 'PC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 2, 'deepskyblue',ifelse(y_grid == 1, 'springgreen3', 'tomato')))
points(set, pch = 21, bg = ifelse(set[, 3] == 2, 'blue3',ifelse(set[, 3] == 1, 'green4', 'red3')))

