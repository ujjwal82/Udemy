# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:55:22 2018

@author: Ujjwal
"""

fridge = dict(apple = 3, banana = 4)

apple_count = fridge['apple']
# 3

coconut_count = fridge['coconut']
# KeyError: 'coconut'

from collections import defaultdict

def zero():
    return 0

#........defaultdict(default_factory, [key-value pairs])
fridge = defaultdict(zero           , apple = 1, banana = 2)
# defaultdict(<function __main__.zero>, {'apple': 1, 'banana': 2})

coconut_count = fridge['coconut']
# 0

# defaultdict(<function __main__.zero>, {'apple': 1, 'banana': 2, 'coconut': 0})

banana_count = fridge['banana']
# 2


fridge = defaultdict(lambda: 0, apple = 1, banana = 2 )
fridge = defaultdict(int      , apple = 1, banana = 2 )



