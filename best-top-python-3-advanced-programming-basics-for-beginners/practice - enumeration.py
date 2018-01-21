# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:06:12 2018

@author: Ujjwal
"""

List = ['First', 'Second', 'Third', 'Forth']

for element in List:
    print(element)

# First
# Second
# Third
# Forth

for element in enumerate(List, start=1):
    print(element)

# (1, 'First')
# (2, 'Second')
# (3, 'Third')
# (4, 'Forth')
    
Number_list = list(enumerate(List, start=1))

# [(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Forth')]
