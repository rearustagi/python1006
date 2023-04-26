# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:58:08 2019

@author: rearu
worked with shivani patel and mallaika tomar
"""

import math
number = int(input("Enter a number: "))
first_int = 1
sum = 1

for x in range(int(math.sqrt(number))):
    if(x <= 1):   
        continue
    if(number % x == 0):
        sum += x
        sum += (number // x)
        
if (sum == number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")

