class Solution:
    def totalNQueens(self, n: int) -> int:
        col = dict()
        pos_dia = dict() # r+c
        neg_dia = dict() # r-c
        
        res = 0
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            for c in range(n):
                if c not in col and (r+c) not in pos_dia and (r-c) not in neg_dia:
                    col[c] = True
                    pos_dia[(r+c)] = True
                    neg_dia[(r-c)] = True
                    
                    backtrack(r+1)
            
                    del col[c]
                    del pos_dia[(r+c)]
                    del neg_dia[(r-c)]
                    
        backtrack(0)
        return res