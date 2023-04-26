# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:00:25 2019

@author: rearu
"""

import random
guessFloat = random.random() * 10 + 1
guess = int(guessFloat)
upperLim = 10
lowerLim = 1
guessedCorrect = False

for i in range(3):
    
    print("My guess is...")
    print(guess)
    print("How was my guess?")
    judge = input("Was it too (B)ig? Too (S)mall? Or just (R)ight? ")
    
    if (judge == 'R'):
        print("The computer wins again!")
        guessedCorrect = True
        break
    elif (judge == 'B'):
        upperLim = guess - 1
        guess = random.randint(lowerLim,upperLim) 
    elif (judge == 'S'):
        lowerLim = guess + 1
        guess = random.randint(lowerLim,upperLim) 
        
print("  ")
if (guessedCorrect == False):
       print("I lost! But I'll get it next time!")
    