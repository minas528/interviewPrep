#!/bin/python3

'''https://www.hackerrank.com/challenges/recursive-digit-sum/problem'''

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    a = str(n)
    sums= 0
    for i in range(len(a)):
        sums += int(a[i])
    print(sums)
    sums = sums*k
    sums = str(sums)
    print(sums)
    while len(sums)>1:
        temp = 0
        for i in range(len(sums)):
            temp += int(sums[i])
        sums = str(temp)
    return sums


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
