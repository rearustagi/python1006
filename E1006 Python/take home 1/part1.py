# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:13:37 2019

@author: rearu
"""

import random
randomFloat = random.random() * 10 + 1
random = int(randomFloat)
guessedCorrect = False

for i in range(5):
   guessStr = input("Guess a number between 1 and 10! ")
   guess = int(guessStr)
    
   if (guess == random):
       print("Congratulations! You won!")
       guessedCorrect = True
       break        
   elif (abs(guess - random) > 5):
       print("Not even close")
   elif (abs(guess - random) <= 5 and abs(guess - random) >= 3):
       print("Close")
   elif (abs(guess - random) < 3):
       print("Almost there!")

print(" ")            
if (guessedCorrect == False):
       print("Sorry! You lose :-( The mystery number was...", random)


