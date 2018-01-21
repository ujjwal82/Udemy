# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:36:08 2018

@author: Ujjwal
"""

'''
the admission fee at a small fair is $1.50 for children and $4.00 for adults.
On a certain day, 2200 people entered the fair and $5050 is collected. How many
adults and how many children attended?

X1 = Number of children, X2 = Number of adults

X1 + X2 = 2200
1.5*X1 + 4*X2 = 5050

A = [ 1,  1    B = [2200,  5050]
     1.5, 4] 
'''

import numpy as np

A = np.array([[1, 1],[1.5, 4]])
B = np.array([2200, 5050])

np.linalg.solve(A, B)

'''
Ans: Children: 1500
     Adults : 700
'''
