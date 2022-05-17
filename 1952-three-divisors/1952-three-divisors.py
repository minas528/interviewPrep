class Solution:
    def isThree(self, n: int) -> bool:
        return 3 == sum(not n%i for i in range(1,n+1))