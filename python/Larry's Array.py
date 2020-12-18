#!/bin/python3

import math
import os
import random
import re
import sys

def ADD(arr, arrlen, idx, val):
    while idx < arrlen:
        arr[idx] += val
        idx += idx & -idx    
    return arr

def SUM(arr, idx):
    result = 0
    while idx:
        result += arr[idx]
        idx -= idx & -idx
    return result

# Complete the larrysArray function below.
def larrysArray(A):
    # Binary Indexed Tree Explain: https://www.youtube.com/watch?v=v_wj_mOAlig&t=1s
    global n
    result = 0
    
    # Create an array with size = n+1
    BIT = [0] * (n+1)
    
    # Caculate Answer by Binary Indexed Tree
    for i in range(n-1, -1, -1):
        result += SUM(BIT, A[i])
        BIT = ADD(BIT, n+1, A[i], 1)
    
    if result % 2 == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
