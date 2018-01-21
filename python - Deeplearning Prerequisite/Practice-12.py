# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:48:05 2018

@author: Ujjwal
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)
y = np.sin(x) + np.sin(x*3) + np.sin(5*x)

plt.plot(y)
plt.show()

Y = np.fft.fft(y)
plt.plot(np.abs(Y))
plt.show()

2*np.pi*48/100
2*np.pi*80/100
