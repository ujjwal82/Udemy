# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 08:46:14 2018

@author: Ujjwal
"""
# Visualization: histogram
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv("data/data_1d.csv", header = None).as_matrix()

x = dataset[:, 0]
y = dataset[:, 1]

plt.hist(x)
plt.hist(y)
plt.show()

R = np.random.rand(10000)
plt.hist(R, bins = 50)
plt.show()

# lets plot histogram of residuals
y_actuals = 2 * x + 1
residuals = y - y_actuals
plt.hist(residuals)
plt.show()