#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l = len(s)
    r = math.floor(math.sqrt(l))
    c = math.ceil(math.sqrt(l))
    o = ''
    
    if r*c < l:
        r += 1
        
    for i in range(c):
        for j in range(r):
            if j*c+i < l:
                o += s[j*c+i]
        o += ' '
    
    return o

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
