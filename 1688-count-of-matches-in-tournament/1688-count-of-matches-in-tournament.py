class Solution:
    def numberOfMatches(self, n: int) -> int:
        num_matches = 0
        while n > 1:
            if (n % 2 == 0):
                n = int(n / 2)
                num_matches = num_matches + n
            else:
                n = (n//2) + 1
                num_matches = num_matches + n - 1
        return num_matches