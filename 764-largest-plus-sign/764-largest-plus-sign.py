class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp, res, ans = [[[0]*4 for _ in range(n)] for _ in range(n)], 0, {(i,j) for i, j in mines}
    
        for i in range(n):
            for j in range(n):
                if (i,j) not in ans:
                    try:
                        dp[i][j][0] = dp[i-1][j][0] + 1
                    except:
                        dp[i][j][0] = 1

                    try:
                        dp[i][j][1] = dp[i][j-1][1] + 1
                    except:
                        dp[i][j][1] = 1


        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i,j) not in ans:
                    try:
                        dp[i][j][2] = dp[i+1][j][2] + 1
                    except:
                        dp[i][j][2] = 1

                    try:
                        dp[i][j][3] = dp[i][j+1][3] + 1
                    except:
                        dp[i][j][3] = 1

                    res = max(res, min(dp[i][j]))

        return res