# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 01:14:21 2018

@author: Ujjwal
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('data/large_files/train.csv')
dataset.shape

M = dataset.as_matrix()
im = M[0,1:]
im
im.shape

im = im.reshape(28, 28)
im
im.shape

plt.imshow(im)
plt.show()
M[0, 0]

plt.imshow(im, cmap='gray')
plt.show()

plt.imshow(255 - im, cmap='gray')
plt.show()
