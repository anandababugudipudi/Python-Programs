# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:51:33 2021

@author: anand
"""

# Lambda arguments:expressoin
x= lambda a:a*a

print (x(3))

#Lambda within user-defined functions

def A(x):
    return (lambda y:x+y)
t = A(4)
print(t(8))

b = A(3)
print (b(9))



# Lambda within filter()
mylist = [1,2,3,4,5,6]
newlist = list(filter(lambda a:(a/3 == 2), mylist)) #SYNTAX: filter(function, iterables)
print(newlist)


List = [1,2,3,4,5,6,7,8,9,10]
newlst = list(filter(lambda a:(a%2 == 0), List))
print(newlst)

#Lambda within map() Syntax: map(func,iterables)
mylist = [1,2,3,4,5,6]
newlist = list(map(lambda a:(a/3 != 2),mylist))
print (newlist)

# Lambda within reduce () Syntax: reduce(function, sequence)
from functools import reduce #import functools or from functools import *
a = reduce(lambda a,b:a+b, [22,34,21,34,45])
print (a)

# Lambda for Algbra
# Linear Equations (having degree one)

s = lambda a:a*a
print (s(4))

# 3x+4y
d = lambda x,y:3*x+4*y
print(d(3,2))

#Quadratic equation ()degree two
#(a+b)^2
x = lambda a,b : (a+b)**2
print (x(2,3))

# Filter within map
c = list (map(lambda x: x+x, filter(lambda x:(x>=4),[2,3,4,5,6])))
print (c)

# Map within Filter
d = list(filter(lambda x: (x % 4 == 0),map(lambda x : (x*2),[1,2,3,4,5,6,7,8,9,10])))
print(d)


from functools import reduce
#Map and Filter within Reduce
r = reduce(lambda x,y:x+y, map(lambda x:x+x, filter (lambda x:(x<=4),[1,2,3,4,5,6,7,8])))

print (r)

































