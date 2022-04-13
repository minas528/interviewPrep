class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r, c = 0, 0
        dr, dc = 0, 1
        res = [[0] * n for _ in range(n)]
        
        for i in range(1, n*n + 1):
            res[r][c] = i   
            
            # at most one right turn
            tmpR, tmpC = r + dr, c + dc
            if (
                tmpR < 0 or tmpR >= n or
                tmpC < 0 or tmpC >= n or 
                res[tmpR][tmpC] != 0
            ):
                dr, dc = dc, -dr # 90 degree clockwise
            
            r, c = r + dr, c + dc
         
        return res