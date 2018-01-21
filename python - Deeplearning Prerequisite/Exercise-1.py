# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:12:41 2018

@author: Ujjwal
"""

import numpy as np

A = np.array([[0.3, 0.6, 0.1],
              [0.5, 0.2, 0.3],
              [0.4, 0.1, 0.5]])

v = np.array([1/3, 1/3, 1/3])


for i in range(25):
    v1 = v.dot(A)
    v = v1
    print(v1)
 