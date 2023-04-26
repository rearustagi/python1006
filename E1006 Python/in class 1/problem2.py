# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:50:24 2019

@author: rearu
worked with shivani patel and mallaika tomar
"""

number_of_seconds = int(input("Enter the number of seconds: "))

number_of_hours = number_of_seconds // 3600
number_of_minutes = (number_of_seconds%3600) // 60
number_of_seconds = (number_of_seconds%3600) % 60

if(number_of_hours == 1):
    print(number_of_hours, " hour, ")
else:
    print(number_of_hours, " hours, ")
    
if(number_of_minutes == 1):
    print(number_of_minutes, " minute, ")
else:
    print(number_of_minutes, " minutes, ")

if(number_of_seconds == 1):
    print(number_of_seconds, " second, ")
else:
    print(number_of_seconds, " seconds.")