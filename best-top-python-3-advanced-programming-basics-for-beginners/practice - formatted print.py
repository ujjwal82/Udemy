# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:10:54 2018

@author: Ujjwal
"""

data = [
        {
                'first'  : 1,
                'second' : 2,
                'third'  : 3,
                'forth'  : 4
        },
        {
                'apple' : 'red',
                'banana' : 'yellow',
                'neste' : {'lvl' : 2}
        },
        {
                'python' : None
        }]
print(data)

from pprint import pprint

pprint(data)
# [{'first': 1, 'forth': 4, 'second': 2, 'third': 3},
# {'apple': 'red', 'banana': 'yellow', 'neste': {'lvl': 2}},
# {'python': None}]

pprint(data, depth = 1)
# [{'first': 1, 'forth': 4, 'second': 2, 'third': 3},
# {'apple': 'red', 'banana': 'yellow', 'neste': {'lvl': 2}},
# {'python': None}]
# [{...}, {...}, {...}]

pprint(data, depth = 2)
# [{'first': 1, 'forth': 4, 'second': 2, 'third': 3},
# {'apple': 'red', 'banana': 'yellow', 'neste': {...}},
# {'python': None}]

pprint(data, depth = 3)
# [{'first': 1, 'forth': 4, 'second': 2, 'third': 3},
# {'apple': 'red', 'banana': 'yellow', 'neste': {'lvl': 2}},
# {'python': None}]


pprint(data, depth = 20)
