# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:41:25 2021

@author: user
"""

import pandas as pd
import numpy as np
import seaborn as sns
import datetime
from datetime import date
import calendar
df=pd.read_csv("C:/Users/user/Desktop/pirple/results.csv")
df.info()
df.head(6)
df.shape
#This dataset includes 42,405 results of international football matches starting from the very first official match in 1972 up to 2019. The matches range from FIFA World Cup to FIFI Wild Cup to regular friendly matches. The matches are strictly men's full internationals and the data does not include Olympic Games or matches where at least one of the teams was the nation's B-team, U-23 or a league select team.
df['date']=pd.to_datetime(df.date)
dw={0:'Monday',1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
df['Day of the week']=df.date.dt.weekday.map(dw)
df
