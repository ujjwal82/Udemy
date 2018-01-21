# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:23:25 2018

@author: Ujjwal
"""


# bool() funciton & truth values


# falsy values - (everything else is true)
bool(False)   # bool
bool(0)       # int
bool(0.0)     # float
bool('')      # string
bool(())      # tuple
bool([])      # list
bool({})      # dici
bool(None)    # Nonetype



bool(2.5)
bool('apple')
bool([1, 2, 3])

# use of bool function
# [if-else] based example 1
if 'expression':
    result = True
else:
    result = False

# [if-else] based example 2
result = True if 'expression' else False

# [bool] based example
result = bool('expression')

# [bool] won't be usefull in many cases, where we want non-bool value

# [if-else] based example 2 - changed
result = 'Something not bool' if 'expression' else False
