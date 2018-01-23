# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:33:19 2018

@author: Ujjwal
"""

import csv

# [example.csv]
# first.row.is.header
# 1.2.3.4_
# 5.6.7
# 9.9.9.9_
# 


with open('example.csv') as f:
    rows = csv.reader(f, delimiter = '.')
    for row in rows:
        print (row)

with open('example.csv') as f:
    rows = csv.reader(f, delimiter = '.')
    header = next(rows); header[0] = 'last'
    for row in rows:
        print(row)
    print(header)

rows = [['header', 'to', 'write'],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]]

with open('write_example.csv', 'w') as f:
    writer = csv.writer(f, delimiter='-', lineterminator = '\n\n')
    writer.writerows(rows)
    writer.writerow(['An', 'extra', 'row'])
    