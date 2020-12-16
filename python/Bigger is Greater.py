#!/bin/python3

import math
import os
import random
import re
import sys

def Swap(w, i, j):
    tmp = w[i]
    w[i] = w[j]
    w[j] = tmp

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    ww = list(w)
    i = len(ww)-2
    while i >= 0 and ww[i] >= ww[i+1]:
        i -=1
    
    if i == -1:
        return 'no answer'
    
    j = len(ww)-1
    while ww[i] >= ww[j]:
        j -= 1
        
    # Swap
    ww[i], ww[j] = ww[j], ww[i]
    
    # Reorder
    ww[i+1:] = ww[len(ww): i: -1]
        
    return ''.join(ww)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
