# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:46:52 2017

@author: Samita
"""

import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;


# importing dataset
dataset = pd.read_csv("data.csv");

# Select all rows and columns except last column
X = dataset.iloc[:,:-1].values

# Select last column of all rows.
y = dataset.iloc[:,3].values

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencode_X = LabelEncoder()
X[:, 0] = labelencode_X.fit_transform(X[:, 0])

onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

labelencode_Y = LabelEncoder()
y = labelencode_Y.fit_transform(y)


# Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X =  StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test= sc_X.transform(X_test)

## If we want to scale only Age and Salary columns
# X_train[:,3:5] = sc_X.fit_transform(X_train[:,3:5])
# X_test[:,3:5] = sc_X.transform(X_test[:,3:5])


