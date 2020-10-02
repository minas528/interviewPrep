'''
    https://leetcode.com/problems/first-missing-positive/submissions/
    41. First Missing Positive

    Given an unsorted integer array, find the smallest missing positive integer.

    Example 1:

    Input: [1,2,0]
    Output: 3
    Example 2:

    Input: [3,4,-1,1]
    Output: 2
    Example 3:

    Input: [7,8,9,11,12]
    Output: 1
    Follow up:

    Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i]=len(nums)+1
        for num in nums:
            num = abs(num)
            if num <= len(nums) and nums[num - 1] >= 0:
                nums[num - 1] *= -1
        # print(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                return k+1
        return len(nums) +1
            