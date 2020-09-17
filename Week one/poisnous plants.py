# slow solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    days = 0
    while True:
        r = []
        for i in range(1,len(p)):
            if p[i]>p[i-1]:
                r.append(i)
        
        if len(r)>0:
            for index in r[::-1]:
                p.pop(index)
            days+=1
        else:
            break        
    return days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
######################################################################################################################

# fast solution

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants2(plants_list):
    stack = []
    maxDyas = -float('inf') 
    for plant in plants_list:
        days = 1
        while stack and stack[-1][0] >= plant:
            _, day = stack.pop()
            days = max(days,day+1)
        if not stack:
            days = 0
        maxDyas = max(maxDyas, days)
        stack.append((plant, days))
    return maxDyas

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
