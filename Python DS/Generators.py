# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:46:44 2021

@author: anand
"""

def new(dict):
    for key, value in dict.items():
        return key, value
    
a = {1:"One", 2:"Two", 3:"Three"}    
b = new(a)

# Generators in loops
def ex():
    n = 3
    yield n
    n = n * n
    yield n
v = ex()
for x in v:
    print (x)    
    
# Generators in expressions
f = range(6)
print ("List comp", end = ":")
q = [x+2 for x in f]
print(q)
print("Generator eXpression ", end =": ")
r = (x+2 for x in f)
for x in r:
    print(x)
    
# Using Generators for finding fibonacci series
def fibonacci():
    f,s = 0,1
    while True:
        yield f
        f,s = s, s+f
for x in fibonacci():
    if x > 50:
        break
    print(x, end=" ")
    
# Number Stream
a = range(100)
b = (x for x in a)
for i in b:
    print(i)
    
# Sinewave
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip = 2):
    x = np.linspace(0, 14, 100)
    for i in range(1, 10):
        yield(plt.plot(x,np.sin(x + i * .5)*(7-i) * flip))
        
sb.set()
s = s()
plt.show()

print(next(s))

    
    
    
    
    
    
    
    
    
    