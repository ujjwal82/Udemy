# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 08:20:50 2018

@author: Ujjwal
"""
import pandas as pd

t1 = pd.read_csv("data/table1.csv",
                engine = "python")
t2 = pd.read_csv('data/table2.csv')

# Lets join these two tables.
# we can achive this by two ways
t3 = pd.merge(t1, t2, on='user_id')
t3

t3 = t1.merge(t2, on='user_id')
t3

