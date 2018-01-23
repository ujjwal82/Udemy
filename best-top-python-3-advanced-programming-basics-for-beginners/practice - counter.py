# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 01:03:55 2018

@author: Ujjwal
"""
from collections import Counter

iterator = ['A', 'B', 'A', 'C', 'D', 'B', 'D', 'E']
counter = Counter(iterator)
# Counter({'A': 2, 'B': 2, 'C': 1, 'D': 2, 'E': 1})

value_of_C = counter['C']
# 1

counter.most_common()
# [('A', 2), ('B', 2), ('D', 2), ('C', 1), ('E', 1)]

counter.most_common(n = 2)
#  [('A', 2), ('B', 2)]

counter.update(['A', 'D'])
# Counter({'A': 3, 'B': 2, 'C': 1, 'D': 3, 'E': 1})

counter.subtract(['B', 'C'])
# Counter({'A': 3, 'B': 1, 'C': 0, 'D': 3, 'E': 1})

counter.subtract({'E' : 100})
# Counter({'A': 3, 'B': 1, 'C': 0, 'D': 3, 'E': -99})

counter2 = Counter(apple=2, banana = 4)
# Counter({'apple': 2, 'banana': 4})
