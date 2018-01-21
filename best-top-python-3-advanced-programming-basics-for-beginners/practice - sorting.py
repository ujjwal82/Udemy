# [Sorting and sorted() function]

# 1 < 2 < 3 < 4 < 5
# True
number_list = [2 ,3 ,4, 5, 1] # iterable

sorted(number_list)
number_list


# ##################################################

# 'A' < 'B' < 'C' < ' D' < 'E' < 'F'
string = "CEDAB"
sorted(string)

sorted(string, reverse = True)
string


# ###################################################

import numpy as np
number_list = np.array( [1, 2, 3, 4, 5])
# distance from 3 : [2, 1, 0, 1, 2]

3 - number_list

def distance_from_3(number):
	return abs(3 - number)


sorted(distance_from_3(number_list))
sorted(number_list, key=lambda number: distance_from_3(number))


