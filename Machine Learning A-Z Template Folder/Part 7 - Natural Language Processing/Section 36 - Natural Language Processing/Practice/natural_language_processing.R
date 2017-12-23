# Natural Language Processing

# Importing the dataset
dataset_original = read.delim('Restaurant_Reviews.tsv', quote = '', stringsAsFactors = FALSE)
names(dataset_original)

# install.packages('tm')
# install.packages('SnowballC')
library(tm)
library(SnowballC)

# Cleaning the text
corpus <- VCorpus(VectorSource(x = dataset_original$Review))

# Convert the text into lower cases
# "Wow... Loved this place." >> "wow... loved this place."
corpus <- tm_map(x = corpus, content_transformer(tolower))

# Remove any number in the review
# "for 40 bucks a head, i really expect better food." >> "for  bucks a head, i really expect better food."
corpus <- tm_map(x = corpus, removeNumbers)

# Remove all punchtuations in the review
# "wow... loved this place." >> "Wow Loved this place"
corpus <- tm_map(x = corpus, removePunctuation)

# Remove all non-relivant in the review
# "Wow Loved this place" >> "wow loved  place"
corpus <- tm_map(x = corpus, removeWords, stopwords())

# Apply steming
# "wow loved  place" >> "wow love place"
corpus <- tm_map(x = corpus, stemDocument)

# Remove extr white spaces from the review
# "wow loved  place" >> "wow love place"
corpus <- tm_map(x = corpus, stripWhitespace)


# Creating bag of words model
dtm <- DocumentTermMatrix(corpus)
dtm <- removeSparseTerms(x = dtm, sparse = 0.999)

dataset <- as.data.frame(as.matrix(dtm))
dataset$Liked <- dataset_original$Liked

# Encoding the target feature as factor
dataset$Liked = factor(dataset$Liked, levels = c(0, 1))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Liked, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

###
# Let's create a dataframe to compare the results from 
# different classification models
###
Comp_results <- data.frame(accuracy = double(), 
                        Recall = double(),
                        Precision = double(),
                        F1Score = double(),
                        G_measure = double()
                        )

dependent_var = 'Liked'
my_model(model_name = 'svm')
my_model(model_name = 'nb')
my_model(model_name = 'dt')
my_model(model_name = 'rf')
my_model(model_name = 'knn')


###
# Function declaration
###
my_model <- function(model_name){

  colIndx <- ncol(test_set)
  lm_formula <- as.formula(paste(dependent_var, ' ~ .', sep = ''))
    
  if(model_name == 'svm'){
    # Fitting SVM model on training set
    library(e1071)
    classifier <- svm(formula = lm_formula, data = training_set)
  }
  if(model_name == 'nb'){
    # Fitting Naive Bayes model on training set
    classifier <- naiveBayes(formula = lm_formula, data = training_set)
  }
  if(model_name == 'dt'){
    # Fitting Decision Tree model on training set
    library(party)
    classifier <- ctree(formula = lm_formula, data = training_set, controls = ctree_control(mincriterion = 0.9, minsplit = 458))
  }
  if(model_name == 'rf'){
    # Fitting Random FOrest model on training set
    library(randomForest)
    classifier <- randomForest(x = training_set[-colIndx], 
                               y = training_set$Liked,
                               ntree = 500)
  }
  if(model_name == 'knn'){
    # Fitting K-NN to the Training set and predicting the Test set results
    #install.packages("class")
    library(class)
    y_pred <- knn(train = training_set[, -colIndx], test = test_set[, -colIndx], 
                  cl = training_set[, colIndx], k = 5)
  }
  
  # Predicting the test set results
  if(model_name != 'knn'){
    y_pred <- predict(classifier, newdata = test_set)
  }
  
  ###
  # Let's caculate different parameters, which 
  # may be used to compare the models
  ###
  # Confussion matrix
  cm <- as.matrix(table(test_set[, colIndx], y_pred)) 
  
  # Calculate other parameters for the model
  model <- as.data.frame(0)
  
  
  # Calculate other parameters for the model
  model <- data.frame(accuracy = (sum(diag(cm))/sum(cm))*100,
                      Recall = cm[1]/  sum(cm[1,]),
                      Precision = cm[1]/ sum(cm[,1]),
                      F1Score = 2*((model$Recall* model$Precision)/(model$Recall + model$Precision)),
                      G_measure = sqrt(model$Recall*model$Precision))
  
  rownames(model) <- c(model_name)

  Comp_results <<- rbind(Comp_results, model)  
  return(model)
}

