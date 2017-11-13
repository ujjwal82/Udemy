# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values


# Encoding categorical data
# Ecoding Independent Variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencode_X = LabelEncoder()
X[:, 3] = labelencode_X.fit_transform(X[:, 3])

onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding dummy variable trap
# First two column with 0,0 represents State: California
X = X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50, 1)), values = X, axis = 1)

X_opt = X[:,[0, 1, 2, 3, 4, 5]]
regressor_OSL = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OSL.summary()

X_opt = X[:,[0, 1, 3, 4, 5]]
regressor_OSL = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OSL.summary()

X_opt = X[:,[0, 3, 4, 5]]
regressor_OSL = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OSL.summary()

X_opt = X[:,[0, 3, 5]]
regressor_OSL = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OSL.summary()

X_opt = X[:,[0, 3]]
regressor_OSL = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OSL.summary()












