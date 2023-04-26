# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:44:23 2019

@author: rearu
worked with shivani patel and mallaika tomar
"""

height = int(input("Please enter the height in cm: "))
width = int(input("Please enter the width in cm: "))
length = int(input("Please enter the length in cm: "))

surface_area_cm = 2*length*height + 2*width*height + width*length
surface_area_m = surface_area_cm/10000
paint_needed = surface_area_m*.25

print("You need ", paint_needed, " liters of paint.")