# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:40:43 2018

@author: Ujjwal
"""

from random import random, uniform, seed, randint, choice, shuffle

# [0..1]
# 0 <= random() < 1.0
random()
# 0.5665334474238791

random()
# 0.30218648435620077


# [Specific range]
# 10 <= uniform (10, 20) < 20
uniform(10, 20)
# 10.863642616748425

uniform(10, 20)
# 15.144884543868429


# [Reproducing the random number ]
seed(1)
random()
# 0.13436424411240122
random()
# 0.8474337369372327

seed(1)
random()
# 0.13436424411240122
random()
# 0.8474337369372327


# [Random Integer]
# 99 <= randint(99, 100) <= 100
randint(99, 100)
# 99
randint(99, 100)
# 100

# [Random items]
colors = ['red', 'blue', 'green', 'yellow', 'purple']
choice(colors)
# 'yellow'
choice(colors)
# 'blue'

shuffle(colors)
colors
# ['blue', 'yellow', 'purple', 'green', 'red']


