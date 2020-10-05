'''
    https://www.hackerrank.com/challenges/jesse-and-cookies/problem
    Jesse and Cookies
'''

import os
import sys
import heapq

#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    heapq.heapify(A)
    res = 0
    while True:
        num = heapq.heappop(A)
        # print(num)
        if num >= k:
            return res 
        if num < k and len(A)<=0:
            return -1
        else:
            num1 = heapq.heappop(A)
            heapq.heappush(A,1*num+2*num1)
            # heapq.heapify(heap)
            res+=1
        
    # heapq.heapify(heap)
    # print(heap)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
