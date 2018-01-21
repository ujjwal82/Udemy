# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 01:22:57 2018

@author: Ujjwal
"""

import numpy as np 
from scipy.stats import norm
import matplotlib.pyplot as plt


norm.pdf(0)
norm.pdf(0, loc = 5, scale = 10)

r = np.random.randn(10)
r
norm.pdf(r)
norm.logpdf(r)

norm.cdf(r)
norm.logcdf(r)

# Visualization
plt.plot(r)
plt.plot(norm.cdf(r))
plt.plot(norm.logcdf(r))
plt.show()

r = np.random.randn(10000)
plt.hist(r, bins = 100)
plt.show()

r = 10 * np.random.randn(10000) + 5
plt.hist(r, bins = 100)
plt.show()

# Gausian distribution
r = np.random.randn(10000, 2)
plt.scatter(r[:,0], r[:, 1])
plt.show()

# Analytical Gausian
r[:, 1] = 5 * r[:, 1] +2
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()


cov = np.array([[1, 0.8],[0.8, 3]])
from scipy.stats import multivariate_normal as mvn

m = np.array([0, 2])
r = mvn.rvs(mean = m, cov=cov, size = 1000)
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()

r = np.random.multivariate_normal(mean = m, cov = cov, size = 1000)
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()
