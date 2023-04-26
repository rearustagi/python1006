# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:18:55 2019

@author: rearu
worked with Mallaika Tomar
"""

def find(s, substring):
    searchLen = len(substring)
    i = 0
    foundStr = False
    
    for letter in s:
        if (substring[0] == letter):
            if (s[i:(i + searchLen)] == substring):
                return(i)
                foundStr = True
                break
        i += 1
                
    if (foundStr == False):
        return(-1)
        
def find_multi(s, substring):
    searchLen = len(substring)
    i = 0
    foundLoci = []
    
    for letter in s:
        if (substring[0] == letter):
            if (s[i:(i + searchLen)] == substring):
                foundLoci.append(i)
        i += 1
                
    return(foundLoci)
    

substring = input("Enter some text that you would like to search for: ")    
s = input("Enter some text that you would like to search in: ")
print("First incidence of your key:", find(s, substring))
print("All incidences of your key:", find_multi(s, substring))