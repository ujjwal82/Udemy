# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 01:10:40 2018

@author: Ujjwal
"""

rectangle = (1, 2)

# (height, width) ?
# or 
# (width, height) ?

height  = rectangle[0]
# height = 1

from collections import namedtuple
Rectangle = namedtuple('Rectangle', 'height width')
rectangle = Rectangle(1, 2)
# Rectangle(height=1, width=2)

height = rectangle.height
# 1

width = rectangle.width
# 2
