# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 08:29:48 2018

@author: Ujjwal
"""

# using visulization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("Code started!!!")
# line plot
x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.plot(x, y)
plt.show()

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Some function of time")
plt.title("My cool chart")
plt.show()

# Scatter chart

dataset = pd.read_csv("data/data_1d.csv", header = None).as_matrix()

x = dataset[:, 0]
y = dataset[:, 1]

plt.scatter(x, y)
plt.show()


x_line = np.linspace(0, 100, 100)
y_line = 2*x_line +1 

plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.show()

print("Finished...")