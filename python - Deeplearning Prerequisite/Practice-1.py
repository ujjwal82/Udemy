 # -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:16:15 2018

@author: Ujjwal
"""
import numpy as np

L = [1, 2, 3]
A = np.array([1, 2, 3])

for e in L:
    print (e)

    
for e in A:
    print (e)

L.append(4)
for e in L:
    print (e)
    
L = L + [5, 6]
for e in L:
    print (e)

L2 =[]
for e in L:
    L2.append(e + e)

L2

A + A
2 * A

2 * L

# doesn't work
#L ** 2

A ** 2
np.sqrt(A)
np.log(A)
np.exp(A)

## ------------------------------- ##
a = np.array([1, 2])
b = np.array([2, 1])

dot = 0
for e, f in (a,b):
    dot += e * f
dot 

a * b
sum(a*b)

(a*b).sum()
np.dot(a, b)

a.dot(b)
b.dot(a)

amag = np.sqrt((a*a).sum())

cosangle = a.dot(b)/ (np.linalg.norm(a) * np.linalg.norm(b))
cosangle

angle = np.arccos(cosangle)
angle

