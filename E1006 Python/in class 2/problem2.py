# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:43:15 2019

@author: rearu
worked with Mallaika Tomar
"""
import re

def print_box(s):
    star = "*"
    space = " "
    maxLength = 0
    final = ""
    
    lines = re.split("\\n | \n", s)
    
    for line in lines:
        testLength = len(line)
        if (testLength > maxLength):
            maxLength = testLength
            
    final += ((star*(maxLength + 2)))
            
    for line in lines:
        testLength = len(line)
        difference = maxLength - testLength
        if (difference % 2 == 0):
            numSpaces = difference // 2
            line = star + space*numSpaces + line + space*numSpaces + star
        else:
            numSpaces1 = difference // 2
            numSpaces2 = difference - numSpaces1
            line = star + space*numSpaces1 + line + space*numSpaces2 + star
        final += "\n" + line
            
    final += "\n" + (star*(maxLength + 2))
    return final
    
s = input("Enter some text that you would like to format: ")
print(print_box(s))