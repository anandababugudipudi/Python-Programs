# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:32:53 2021

@author: anand
"""


my_list = [1,2,3,4,5,6]

import numpy as np
array = np.array(my_list, dtype = int)

print (array)
print (type(array))
print (len(array))
print (array.ndim)
print (array.shape)


array2 = array.reshape(3,2)
print (array2)
array2.shape

array3 = array.reshape(3,-1)
print (array3)
print (array3.ndim)


my_list1 = [1,2,3,4,5]
my_list2 = [2,3,4,5,6]
my_list3 = [9,2,3,4,8]

mul_arr = np.array([my_list1, my_list2, my_list3])
print (mul_arr)
print (mul_arr.ndim)

print (mul_arr.shape)
mul_arr.reshape(1,15)
print (mul_arr.shape)

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
a.shape = (3,2)
print(a)
a.shape = (6,-1)
print(a)



a = np.arange(24)
print(a)
print(a.ndim)

b = a.reshape (6,2,2)
print(b)




x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x)
print(y)
print("Performing addition operation")
print (x+y)
print (np.add(x,y))

print("Performing substraction operation")
print (x-y)
print (np.subtract(x,y))

print("Performing multiplication operation")
print (x*y)
print (np.multiply(x,y))

print("Performing dot operation")
print (x.dot(y))
print (np.dot(x,y))

print("Performing division operation")
print (x/y)
print (np.divide(x,y))


print(x)
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))



my_dict = {'Dave':'001','Ava':'002','Brij':'003','Charlie':'004'}
emp_details = {'Dev Team':{'Berth':{'ID':'002', 'Salary':'2000', 'Designation':'Team Lead'}}}
               
               # ,{'Ciara':{'ID':'003', 'Salary':'2000', 'Designation':'Developer'}}}

print (emp_details)

print ("Dictionary : {}".format(my_dict))
print ("Keys : {}".format(my_dict.keys()))
print ("Values : {}".format(my_dict.values()))

print (my_dict.get('Ava'))


for x in my_dict.values():
    print(x)

for x,y in my_dict.items():
    print (x,y)


my_dict['Dave']='009'
my_dict['Emma']='007'

print (my_dict.pop('Ava'))

my_dict.popitem()

del my_dict['Brij']

print (my_dict)

'''

import pandas as pd
df = pd.DataFrame(emp_details['Dev Team'])
print (df)



