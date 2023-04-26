# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:09:31 2019

@author: rearu
worked with Mallaika Tomar
"""

def piggify(word):
    
    vowels = "aeiou"
    pig = ""
    counter = 0
    
    if (word[0] in vowels):
        pig = word + "yay"
    else:
        for char in word:
            if (char in vowels):
                break
            else:
                counter += 1
        pig = word[counter:] + word[:counter] + "ay"
        
    return(pig)

while True:
    word = input("What is the word you want to piggify? ")
    if (word == "."):
        break
    print("Translation in pig latin:", piggify(word))
    