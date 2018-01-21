# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:45:16 2018

@author: Ujjwal
"""

import numpy as np

# Matrix multiplication

A = np.array([[1, 2], [3, 4]])
print('A: ', A)

Ainv = np.linalg.inv(A)
print('Ainv: ', Ainv)

Ainv.dot(A)
A.dot(Ainv)

# determinant of matrix
# Matrix needs to be a square matrix
np.linalg.det(A)

B = np.array([[1, 2, 3],[4, 5, 6],  [7, 8, 9]])
np.linalg.det(B)

np.linalg.eig(B)
np.linalg.eig(A)
np.linalg.eigh(B)

# diagonals of 2-D array
np.diag(B)

# diagonal of 1D array
C = np.array([1,2])
np.diag(C)

# inner/outer product

a = np.array([1, 2])
b = np.array([3, 4])

np.outer(a, b)

# np.inner and dot gives same result
np.inner(a, b)
a.dot(b)

# Summation of diagonal elements
A = np.array([[1, 2], [3, 4]])
np.diag(A).sum()

np.trace(A)

# Covariance
X = np.random.randn(100, 3)
cov = np.cov(X)

cov.shape
X.T
cov = np.cov(X.T)
cov.shape
cov

# Eigen value and Eigen vectors
np.linalg.eig(cov)

A = np.array([[1,2],[3,4]])
B = np.array([1,2])

x = np.linalg.inv(A).dot(B)
x
np.linalg.solve(A, B)
