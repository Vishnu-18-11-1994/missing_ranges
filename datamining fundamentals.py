# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:56:56 2021

@author: user
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
cricketers_data=pd.read_excel("C:\\Users\\user\\Desktop\\Vishnu\\Datasets\\ICC Test Bat 3001.xlsx")
cricketers_data.shape
cricketers_data.info
cricketers_data.describe()
cricketers_data.head()
cricketers=cricketers_data.drop('Player Profile', axis=1)
cricketers
df=cricketers.head(30)
df
