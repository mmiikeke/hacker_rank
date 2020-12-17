#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    global H, W
    result = 0

    # Up surface, down surface
    result += H*W*2

    # Left surface, right surface
    for i in range(H):
        for j in [0, W-1]:
            result += A[i][j]

    # Front surface, back surface
    for i in [0, H-1]:
        for j in range(W):
            result += A[i][j]

    # Inner left-right surface
    for i in range(H):
        for j in range(W-1):
            result += abs(A[i][j] - A[i][j+1])

    # Inner front-back surface
    for i in range(H-1):
        for j in range(W):
            result += abs(A[i][j] - A[i+1][j])

    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
