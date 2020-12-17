#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return [i+1 for i in range(n)]
    
    if k > (n+1)//2:
        return [-1]
    
    if (n%(k*2)) != 0:
        return [-1]
    
    result = list()
    
    for i in range((n//k)//2):
        for j in range(k):
            result.append(i*2*k+1+k+j)
        for j in range(k):
            result.append(i*2*k+1+j)
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
