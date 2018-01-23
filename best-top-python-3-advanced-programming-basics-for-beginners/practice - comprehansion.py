# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:08:18 2018

@author: Ujjwal
"""

# ===============================================
#  Comprehansion
# ===============================================

# Sotre elelments in a container:
# ==============================
# 1. Initiate an empty container
# 2. Add elements to the container

numbers_1_to_5 = []
numbers_1_to_5.append(1) 
numbers_1_to_5.append(2) 
for number in range(3, 5+1):    # +1 needed because range's end is exclusive.
    numbers_1_to_5.append(number) 

numbers_1_to_5.append

# ============================================================================
#                    [Comprehansions 2 responsibilities]
#  1. Data structure creation             2. provide proper elements to store  
#
# ============================================================================
#
#  |-------------------------------------------------------------------|
#  | Comprehansion | Syntax                 | Syntax with predicate    |
#  |-------------------------------------------------------------------|
#  | list          | [o for v in i]         | [o for v in i if p]      |
#  | set           | {o for v in i}         | {o for v in i if p}      |
#  | generator     | (o for v in i)         | (o for v in i if p)      |
#  | dict          | {ok:ov for v in i}     | {ok:ov for v in i if p}  |
#  |-------------------------------------------------------------------|
#  o : output_expression
#  v : variable
#  i : input_iterator
#  ok: output key
#  ov: output value
#
# ============================================================================

iterable = 1, 2, 3, 4    # tupple of (1, 2, 3, 4) is an iterable

multiplied_list = list(map(lambda num: 5 * num, iterable))
# [5, 10, 15, 20]

multiplied_list  = [5 * num for num in iterable]
# [5, 10, 15, 20]

multiplied_generator = (5 * num for num in iterable)
# <generator object <genexpr> at 0x000001BBB9AACC50>

next(multiplied_generator)
# 1st next() : 5
# 2nd next() : 10
# 3rd next() : 15
# 4th next() : 20

multiplied_dict = {num : 5 * num for num in iterable}
# {1: 5, 2: 10, 3: 15, 4: 20}

# Let's see how do they work when we use predicates

iterable = 1, 2, 3, 4

filtered_multiplied_list = list(map(lambda num: 5 * num,
                                    filter(lambda num: num % 2 ==0, iterable)))
# [10, 20]

filtered_multiplied_list = [ 5 * num for num in iterable if num % 2 == 0] 
# [10, 20]


# Nesting comprehansion
letters = 'A', 'B', 'C', 'D'
numbers = '1', '2', '3', '4'

# combined_lists
# [['A1', 'B1', 'C1', 'D1'],
#  ['A2', 'B2', 'C2', 'D2'],
#  ['A3', 'B3', 'C3', 'D3'],
#  ['A4', 'B4', 'C4', 'D4']]


combined_lists = []
for number in numbers:
    combined_list = []
    for letter in letters:
        combined_list.append(letter + number)
    combined_lists.append(combined_list)


combined_lists = [[letter + number for letter in letters ] for number in numbers]






