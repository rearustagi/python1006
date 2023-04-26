# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:33:06 2019

@author: rearu
"""

def read_markets(filename):
    
    zip_dict = dict()
    town_dict = dict()
    
    market_file = open(filename,'r')
    for line in market_file:
        x = line.split("#")
        x[4] = x[4].zfill(5)
        t = tuple(x[0:5])
        mzip = t[4]
        mtown = t[3]
        
        if mzip != '00000':
            if mzip not in zip_dict.keys():
                zip_dict[mzip] = [t]
            else:
                zip_dict[mzip].append(t)
            if mtown not in town_dict.keys():
                town_dict[mtown] = {mzip}
            else:
                town_dict[mtown].add(mzip)

    return zip_dict, town_dict

def print_market(market):
    
    f = "{}\n{}\n{}, {} {}"
    fstring = f.format(market[1], market[2], market[3], market[0], market[4])
    
    return fstring

if __name__ == "__main__":

    FILENAME = "markets.txt"
    ask = True

    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)
        while ask:
            lookFor = input("By which ZIP code or town would you like to search for farmer's markets? Type 'quit' to stop searching.\n")
            if lookFor == "quit":
                ask = False
                print("Happy shopping!")
                break
            else:
                try:
                    test = int(lookFor)
                    print("\nHere are the farmer's markets near you:")
                    for each in zip_to_market[lookFor]:
                        print('\n' + print_market(each))        
                except ValueError:
                    try:
                        print("\nHere are the farmer's markets near you:")
                        for eachZIP in town_to_zips[lookFor]:
                            for each in zip_to_market[eachZIP]:
                                print('\n' + print_market(each))
                    except (KeyError):
                        print("None found.")  
                except (KeyError):
                    print("None found.")
                    
    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
