class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        f = [0]*(target+1)
        for j in nums:
            if j <= target:
                f[j]=1
        nums.sort()
        for i in range(1, target+1):
            for j in nums:
                if j <= i:
                    f[i] += f[i-j] 
        return f[-1]