#!/bin/python3

import math
import os
import random
import re
import sys

def Explode(grid):
    result = list()
    for i in range(r):
        string = ''
        for j in range(c):
            flag = 0
            
            if grid[i][j] == 'O':
                flag = 1
            if i-1 >= 0 and grid[i-1][j] == 'O':
                flag = 1
            if j-1 >= 0 and grid[i][j-1] == 'O':
                flag = 1
            if i+1 < r and grid[i+1][j] == 'O':
                flag = 1
            if j+1 < c and grid[i][j+1] == 'O':
                flag = 1
            
            if flag == 1:
                string += '.'
            else:
                string += 'O'
        result.append(string)
    
    return result

# Complete the bomberMan function below.
def bomberMan(n, grid):
    global r, c
    result = list()
    
    if n%2 == 0:
        string = ''
        for i in range(c):
            string += 'O'
        for i in range(r):
            result.append(string)
        return result
    
    if n == 1:
        return grid
    
    if (n+1)%4 == 0: #n=3,7,11,15,...
        return Explode(grid)
    else: #n=5,9,13,17,...
        return Explode(Explode(grid))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
