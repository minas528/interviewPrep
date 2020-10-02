'''
    https://leetcode.com/contest/weekly-contest-184/problems/number-of-ways-to-paint-n-3-grid/
    1411. Number of Ways to Paint N × 3 Grid
'''
class Solution:
    def numOfWays(self, n: int) -> int:
        head, tail = 6, 6
        if n == 1:
            return head + tail
        for i in range(2, n+1):
            nex_h = (3 * head + 2* tail) % (10**9 +7)
            nex_t = (2 * head + 2* tail) % (10**9 +7)
            head , tail= nex_h , nex_t
        return ((head+tail)%(10**9 +7))
            