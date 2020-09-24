'''
    https://leetcode.com/problems/k-th-symbol-in-grammar/
    779. K-th Symbol in Grammar
    On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

    Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

    Examples:
    Input: N = 1, K = 1
    Output: 0

    Input: N = 2, K = 1
    Output: 0

    Input: N = 2, K = 2
    Output: 1

    Input: N = 4, K = 5
    Output: 1

    Explanation:
    row 1: 0
    row 2: 01
    row 3: 0110
    row 4: 01101001
    Note:

    N will be an integer in the range [1, 30].
    K will be an integer in the range [1, 2^(N-1)].
'''
# bruet force solution- TLE
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        s ='0'
        for i in range(1, N):
            n = ''
            for j in range(len(s)):
                
                if s[j] == '0':
                    n+= '01'
                elif s[j] == '1':
                    n+= '10'
            s = n
        
        print(s)
        return int(s[K-1])

# optimal solution ACEPTED
class Solution2:
    def kthGrammar(self, N: int, K: int) -> int:
        similar = 1
        for i in range(N-1):
            if K%2 == 0:
                similar = -similar
                K/=2
            else:
                K= (K+1)/2
        return 0 if similar==1 else 1
    