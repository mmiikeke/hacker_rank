#!/bin/python3

import math
import os
import random
import re
import sys

def Caculate(a, r, c, rr, cc):
    dr = rr-r
    dc = cc-c
    
    if rr < 0 or cc < 0 or rr > n or cc > n:
        return a
    
    if abs(dr) == abs(dc):
        if dr > 0 and dc > 0:
            a[4] = min(a[4], dc-1)
        elif dr < 0 and dc > 0:
            a[5] = min(a[5], dc-1)
        elif dr < 0 and dc < 0:
            a[6] = min(a[6], -dc-1)
        elif dr > 0 and dc < 0:
            a[7] = min(a[7], -dc-1)
    elif dr > 0 and dc == 0:
        a[0] = min(a[0], dr-1)
    elif dr == 0 and dc > 0:
        a[1] = min(a[1], dc-1)
    elif dr < 0 and dc == 0:
        a[2] = min(a[2], -dr-1)
    elif dr == 0 and dc < 0:
        a[3] = min(a[3], -dc-1)       
    
    return a
    
# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    r = r_q
    c = c_q
    # up right down left (up right) (right down) (down left) (left up)
    a = [n-r, n-c, r-1, c-1, min(n-r, n-c), min(n-c, r-1), min(r-1, c-1), min(c-1, n-r)]
    o = 0

    if r < 0 or c < 0 or r > n or c > n:
        a = [0]*8
    
    for i in obstacles:
        a = Caculate(a, r, c, i[0], i[1])

    for i in a:
        o += i
        
    return o
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
