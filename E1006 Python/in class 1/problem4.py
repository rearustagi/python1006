# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:04:12 2019

@author: rearu
worked with mallaika tomar
"""

li = []
smallNums = []

print("Please pick some numbers to add to the list.")
print("Input any letter to stop adding numbers.")

while True:
    addMe = input("Enter a number: ")
    try:
        val = int(addMe)
        li.append(val)
    except ValueError:
        break
    
print("Your list is:", li)
    
k = int(input("How many of the smallest values do you want? "))

for x in range(k):
    minIndex = li.index(min(li))
    smallNums.append(li[minIndex])
    li.pop(minIndex)
    
print("The", k, "smallest integers are:", smallNums)