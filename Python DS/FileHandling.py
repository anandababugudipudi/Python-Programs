# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:44:53 2021

@author: anand
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:28:12 2021

@author: anand
""" 
# File Handling
import os

file = open ("Python/testfile.txt","r")

print (file.read())

print(file.readline())

print(file.readline(3))

print(file.readlines())

for line in file:
    print(file.readlines())

file.close()
    


file = open ("Python/testfile.txt","a")

file.write ("Hello world")

file.close()
 
file = open ("Python/test.txt","x")

file.write ("Hello world")

file.close()


# Deleting file
FileName = "Python/taste.txt"
if os.path.exists (FileName):
    os.remove(FileName)
else:
    print("The file doesn't exist.")

# Deleting a directory
os.rmdir (FolderName)


































