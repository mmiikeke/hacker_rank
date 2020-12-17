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

# Complete the insertionSort function below.
def insertionSort(arr):
    # Explain: https://www.youtube.com/watch?v=v_wj_mOAlig&t=1s
    global n
    result = n*(n-1)//2
    
    # Find maximum element in arr
    maxnum = 0
    for i in arr:
        if i > maxnum:
            maxnum = i
    
    # Create an array with size = maxnum+1
    BIT = [0] * (maxnum+1)
    length = maxnum+1
    
    # Caculate Answer by Binary Indexed Tree
    for i in arr:
        result -= SUM(BIT, i)
        BIT = ADD(BIT, length, i, 1)
    
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
