class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        dp = [[0]*(l1+1) for i in range(l2+1)]
        res = 0

        for i in range(l2-1, -1, -1):
            for j in range(l1-1, -1, -1):
                if word2[i]==word1[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                res = max(res, dp[i][j])
        return l1+l2-2*res