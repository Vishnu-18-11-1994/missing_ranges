# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 08:59:34 2021

@author: user
"""

import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x)

#dates
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%c"))
print(x.strftime("%b"))

for x in range(100):
    print(max(x))
x=-7.25
print(abs(x))

#math
import math
x=dir(math)
print(x)


#json
import json
a='{"vishnu":26, "sachin":48}'
x=json.loads(a)
print(x)

b={"name":"vishnu", "age":26}
y=json.dumps(b)
print(y)
type(y)


#try, except and exceute blockx
try:
    print(x)
except:
    print("if everything is set")
else:
    print("not ifine")