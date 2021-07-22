# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:05:17 2021

@author: user
"""



import pandas as pd
a={"cricketers":["sachin", "virat","dhoni"], "tennis": ["federer", "nadal", "djokovic"]}
b=pd.DataFrame(a)
print(b)
a=[1,2,3]
print(pd.Series(a, index=["x", "y", "z"]))
fab4={"virat":[153,7490,52.38,27], "smith":[139,7540,61.8,27], "root":[189,8617,48.96,20],"williamson":[145,7128,54.00,24]}
modernday_legends=pd.DataFrame(fab4,index=("innings","runs","avg","centuries"))
print(modernday_legends)


#string inbuilt functions
name="vishnu"
name.capitalize()
name.casefold()
name.center(3)
name.count()
_name=[1,2]
"hello"[0]
