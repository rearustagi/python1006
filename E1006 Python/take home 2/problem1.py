# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:23:54 2019

@author: rearu
"""

def dressing():
    dressing = input("Choose from: vinaigrette, ranch, blue cheese, and lemon.\n")
    return dressing

def toppings():
    toppings = []
    while True:
        topping = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done':\n")
        if (topping == "done"):
            break
        toppings.append(topping)
    allTop = " and ".join(each for each in toppings)
    return allTop
        
def salad():
    choice = input("Would you like a garden or greek salad?\n")
    f = "What kind of dressing would you like with your {} salad?"
    print(f.format(choice))
    dressingChoice = dressing()
    saladForm = "a {} salad with {} dressing"
    return saladForm.format(choice, dressingChoice)
    
    
def pizza():
    choice = input("What size pizza would you like: small, medium, or large?\n")
    f = "What kind of toppings would you like on your {} pizza?"
    print(f.format(choice))
    toppingChoice = toppings()
    pizzaForm = "a {} pizza with {}"
    return pizzaForm.format(choice, toppingChoice)

def select_meal():
    order = []
    while True:
        start = input("Hello, would you like pizza or salad?\n")
        if (start == "pizza"):
            pizzaOrder = pizza()
            order.append(pizzaOrder)
        elif (start == "salad"):
            saladOrder = salad()
            order.append(saladOrder)
        summary = "\nGreat, here's your order so far: {}."
        series = " and ".join(each for each in order)
        print(summary.format(series))
        addMore = input("Place another order by pressing any key or say 'done'.\n")
        if (addMore == "done"):
            break
    print("\nThanks for your order!")
                  
    
select_meal()