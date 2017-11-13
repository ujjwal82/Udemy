# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:46:52 2017

@author: Ujjwal Kumar
"""

import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;


# importing dataset
dataset = pd.read_csv("data.csv");

# Select all rows and columns except last column
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)

# feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X =  StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test= sc_X.transform(X_test)
"""


