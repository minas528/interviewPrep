class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        end = 0
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        start = len(nums) - 1
        prev = nums[start]
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        return end - start +1 if end != 0 else 0