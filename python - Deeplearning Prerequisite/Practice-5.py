# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:45:46 2018

@author: Ujjwal
"""
import numpy as np

X = []
for line in open("../machine_learning_examples/linear_regression_class/data_2d.csv"):
    row = line.split(',')
    sample = list(map(float, row))
    X.append(sample)
X
X = np.array(X)
X.shape

# Read the file using Pandas

import pandas as pd

X = pd.read_csv("data/data_2d.csv",
                header = None)

X.shape
X.info()
X.head()
X.head(10)

M = X.as_matrix()
type(M)

X[0]
M[0]

# retrieve First column data
X[0]

# Retrieve First row data
X.iloc[0]

# types of row data and column data
type(X[0])
type(X.iloc[0])

# Select more than one column, i.e: select first and third column
X[[0,2]]

# Conditinal selction
# select all of the rows with data for the 0th column <5
X[ X[0] < 5]


