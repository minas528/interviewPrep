#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    n=len(arr)
    for l in arr:
        l[0] = int(l[0])  
                
    for i in range(n//2): 
        arr[i][1] = "-"
        
    output = [[] for _ in range(n)]
    # print(output)
    for l in arr:
        output[l[0]].append(l[1])
        print(output)
        
    print(' '.join(j for i in output for j in i))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
