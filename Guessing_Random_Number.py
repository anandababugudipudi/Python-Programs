# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:19:15 2021

@author: anand
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:28:12 2021

@author: anand
"""

import random
Min = 1
Max = 10
n = random.randint(Min, Max)
guess = 0
while guess != n:
    guess = int(input("Enter the number: "))
    if ( Min < guess < Max):
        if guess < n:
            print ("Guessed number is too small")
        elif n < guess:
            print ("Guessed number is too big")
    else:
        print ("Enter numbers between {} and {}".format(Min, Max))        
else:
    print ("Congratulations you have made it!")
        
# print (n)