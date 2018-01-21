# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 00:07:59 2018

@author: Ujjwal
"""

from __future__ import print_function, division
import pandas as pd

df = pd.read_csv("data/international-airline-passengers.csv",
                engine = "python",
                skipfooter = 3)
df.shape

df.columns = ["month", "passengers"]

df['passengers']
df.passengers

# add new column
df['one'] = 1
df.head()

from datetime import datetime

datetime.strptime("1949-05", "%Y-%m")

df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis = 1)

# using use defined function call
def get_date(row):
    return (datetime.strptime(row['month'], '%Y-%m'))

df['dt'] = df.apply(get_date, axis = 1)
df.info()

