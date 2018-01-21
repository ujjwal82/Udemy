# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:11:45 2018

@author: Ujjwal
"""
import numpy as np

# Matrix
M = np.array([[1, 2], [3, 4]])
M

L = [[1, 2], [3, 4]]
L

L[0]
L[0][0]

M[0][0]
M[0, 0]

M2 = np.matrix([[1, 2], [3, 4]])
M2

# Create matrix of random numbers
np.array([1, 2, 3])

Z = np.zeros(10)

Z1 = np.zeros((10, 10))
Z1

Z2 = np.ones((10, 10))
Z2[0]

R = np.random.random((10, 10))
R

G =  np.random.randn(10, 10)
G
G.mean()
G.var()


