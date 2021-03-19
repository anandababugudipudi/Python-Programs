# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:35:46 2021

@author: anand
"""
'''
# =============================================================================
# Class Creatio
# =============================================================================

class Employee():
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        
Andy = Employee('Andy', 23000, 25)
Brij = Employee('Brij', 22000, 26)
Cind = Employee('Cind', 28000, 23)

print(Andy.__dict__)
print(Brij.salary)

# =============================================================================
# Inheritance
# =============================================================================

class Car():
    def __init__(self, modelname, year, price, cc):
        self.modelname = modelname
        self.year = year
        self.price = price
        self.cc = cc
        
class SuperCar(Car):
    def __init__(self, modelname, year, price, cc):
        super().__init__(modelname, year, price, cc)

honda = SuperCar('City', 2017, 10000, 1500)
tata = Car('Tiago', 2015, 6000, 1200)

print(honda.modelname)
print(tata.modelname)

# Syntax for Polymorphism and child class
class parentClass():
    def __init__(self, instance1, instance2, instance3):
        self.instance1 = instance1
        self.instance2 = instance2
        self.instance3 = instance3
        
class childClass(parentClass):
    def __init__(self, instance1, instance2, instance3):
        super().__init__(instance1, instance2, instance3)
        
object1 = parentClass(111, 112, 113)

print(object1.instance1)
    

# =============================================================================
# # Abstraction
# =============================================================================
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def priceIncrease(self):
        pass
    
class SuperCar(Car):
    def __init__(self, modelname, year, price, cc):
        super().__init__(modelname, year, price, cc)
    def priceIncrease(self):
        self.price = int(self.price*2)
    
honda = SuperCar('City', 2017, 10000, 1500)
tata = Car('Tiago', 2015, 6000, 1200)

print(honda.modelname)
print(honda.price)
honda.priceIncrease()
print(honda.price)
print(tata.modelname)



# =============================================================================
# Encapsulation
# =============================================================================
# =============================================================================
# # Python program to demonstrate protected members
# =============================================================================
# Creating a base class
class Base:
	def __init__(self):
		
		# Protected member
		self._a = 2

# Creating a derived class 
class Derived(Base):
	def __init__(self):
		
		# Calling constructor of
		# Base class
		Base.__init__(self) 
		print("Calling protected member of base class: ")
		print(self._a)

obj1 = Derived()
		
obj2 = Base()

# Calling protected member
# Outside class will result in 
# AttributeError
print(obj2.a)


# =============================================================================
# # Python program to demonstrate private members
# =============================================================================
# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):
		# Calling constructor of Base class
		Base.__init__(self) 
		print("Calling private member of base class: ")
		print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class 
# is called inside derived class

'''
# =============================================================================
# Inheratance: Overloading Parent Class
# =============================================================================
# Parent Class
class Parent():
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage
    def view(self):
        print(self.name, self.age)
# Child Class
class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "python"
        
    def view(self):
        print(self.name, self.age, self.lastname)
        
obj1 = Child(23, 'Hello')
        
obj1.view()











