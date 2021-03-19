# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:32:19 2021

@author: anand
"""

# First class objects, using functions as arguments

def func1(name):
    return f"Hello {name}"

def func2(name):
    return f"{name}, how you doing?"

def func3(func4):
    return func4("Dear Learner")

print(func3(func1))
print(func3(func2))


# Inner functions or Nested function
def func():
    print("First function.")
    def func1():
        print("First child function")
    def func2():
        print("Second child function")
    
    func2()
    func1()        
    
func()


def func(n):
    def func1():
        return "Edureka"
    def func2():
        return "Python"
    if n == 1:
        return func1()
    else:
        return func2()
    
a = func(1)
b = func(3)

print (a)
print (b)

# Decorator functions

def header(name):
    def wrapper():
        print("Hello")
        name()
        print("Welcome to Python Course.")
    return wrapper
def returnName():
    print("User")

returnName = header(returnName) #wrapper text

returnName()

#Using Syntactic Sugar in Decorator

def header(name):
    def wrapper():
        print("Hello")
        name()
        print("Welcome to Python Course.")
    return wrapper
@header           #Syntactic Sugar
def returnName():
    print("User")

returnName()
 
   
# Using arguments in function
def header(name):
    def wrapper(*args, **kwargs):
        print("Hello")
        name(*args, **kwargs)
        print("Welcome to Python Course.")
    return wrapper
@header           #Syntactic Sugar
def returnName(name):
    print(f"{name}")

returnName("Google")
    

# Returning arguments

def header(name):
    def wrapper(*args, **kwargs):
        print("Hello")
    return wrapper
@header           #Syntactic Sugar
def returnName(name):
    print(f"{name}")

returnName("Google")


import functools

# Class objects
class Square:
    def __init__(self, side):
        self._side = side
        @property
        def side(self):
            return self._side
        @side.setter
        def side(self, value):
            if value >= 0:
                self._side = value
            else:
                print("Error")
        @property
        def area(self):
            return self._side ** 2
        @classmethod
        def unit_square(cls):
            return cls(1)
s = Square(5)
print (s.side)
print (s.area)


# Singleton Class

def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper
@singleton
class one:
    pass
first = one()
second = one()

print(first is second)
    

# Nesting Decorators

def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(num = 5)
def function (name):
    print(f"{name}")            

function("Python")










    










































