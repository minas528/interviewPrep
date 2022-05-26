class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(i) for i in bin(n) if i=='1'])