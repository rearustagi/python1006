# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:03:43 2019

@author: rearu
"""

from collections import defaultdict
import string

def count_ngrams(file_name, n): 
    
    read_file = open(file_name,'r', encoding='utf-8')
    processed = []
    
    for line in read_file:
        line = line.strip()
        words = line.split()
        
        for word in words:
            pword = word.strip(string.punctuation)
            processed.append(pword.lower())
            
    ngrams = []
    counter = 0
    for elem in processed:
        ngram = tuple(processed[counter:counter+n])
        if len(ngram) == n:
            ngrams.append(ngram)
        counter += 1
        
    freq = defaultdict(int)
    for item in ngrams:
        freq[item] += 1

    return freq

def single_occurences(ngram_count_dict): 
    
    singleOcc = []
    for key in ngram_count_dict.keys():
        if ngram_count_dict[key] == 1:
            singleOcc.append(key)
    
    return singleOcc

def most_frequent(ngram_count_dict, num): 
    
    list = [(k, v) for v, k in ngram_count_dict.items()] 
    list = sorted(list, reverse = True)
    x = list[:num]
    phrases = []
    for elem in x:
        phrases.append(elem[1])
        
    return phrases

def main():
    filename = "manifesto.txt"
    n = int(input("What n-gram would you like to find? Type a number:\n"))
    most_frequent_k = int(input("How many of the most frequent n-grams would you like to search for? Type a number:\n"))

    ngram_counts = count_ngrams(filename, n)

    print('{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))

    print('\n{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))

if __name__ == "__main__":
    main()
