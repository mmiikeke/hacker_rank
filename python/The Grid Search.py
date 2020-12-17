#!/bin/python3

import math
import os
import random
import re
import sys

def Search(ii, jj, G, P):
    global r, c
    
    for i in range(r):
        for j in range(c):
            if P[i][j] != G[i+ii][j+jj]:
                return False
    
    return True

# Complete the gridSearch function below.
def gridSearch(G, P):
    global R, C, r, c
    
    dr = R-r+1
    dc = C-c+1

    for i in range(dr):
        for j in range(dc):
            if Search(i, j, G, P):
                return 'YES'
                
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
