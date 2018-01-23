# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:05:05 2018

@author: Ujjwal
"""

#   [iterable]   =====>  [new iterable]
#  --------------       ------------------
#  | element 1  |  =>   | new element 1 | 
#  | element 2  |  =>   | new element 2 | 
#  | element 3  |  =>   | new element 3 | 
#  | ...        |  =>   | ...           | 
#  | element N  |  =>   | new element N | 
#  --------------       -----------------

iterable  = [1, 2, 3, 4]

# [Goal]
# List: [5, 10, 15, 20]

List = []
for number in iterable:
    List.append(number * 5)

#  [5, 10, 15, 20] 

# here is how we can do this using MAP function
List = list(map(lambda n: n*5, iterable))


def multiply_by_5(number):
    return number * 5

List = list(map(multiply_by_5, iterable))

