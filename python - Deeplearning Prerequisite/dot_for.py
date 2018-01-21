# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:41:03 2018

@author: Ujjwal
"""

from __future__ import print_function, division
from builtins import range

import numpy as np
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

def slow_dot_product(a, b):
    result = 0
    for e, f in zip(a, b):
        result += e * f
    return result

t0 = datetime.now()
for t in range(T):
    slow_dot_product(a, b)

dt1 = datetime.now() - t0

 
t0 = datetime.now()
for t in range(T):
    a.dot(b)

dt2 = datetime.now() - t0

print("dt1 / dt2: ", dt1.total_seconds() / dt2.total_seconds())
