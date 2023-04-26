# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:33:49 2019

@author: rearu
"""
import numpy as np

a = np.array([[1,2,3,4,5,6],
              [1,2,3,4,5,6],
              [1,2,3,4,5,6],
              [1,2,3,4,5,6],
              [1,2,3,4,5,6]])

def path_sum(a, moves):
    sum = a[0][0]
    row = 0 
    col = 0
    for move in moves:
        if move == 'right':
            col = col + 1
        elif move == 'left':
            col = col - 1
        elif move == 'up':
            row = row - 1
        elif move == 'down':
            row = row + 1
        else:
            print('invalid input')
        
        current = a[row][col]
        sum = sum + current
        
    return sum

print(path_sum(a, ['left']))

