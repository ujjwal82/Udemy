# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:13:41 2018

@author: Ujjwal
"""

iterable_list = [1, 2, 3, 4]

number_greater_than_2 = []
for n in iterable_list:
    if(n > 2):
        number_greater_than_2.append(n)


# []
# [3]
# [3, 4]

number_greater_than_2  = []
number_greater_than_2  = list(filter(lambda n: n > 2, iterable_list))




