'''
    https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
    215. Kth Largest Element in an Array
    Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Example 1:

    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
    Example 2:

    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4
    Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return -res

# Alt solution
        # arr = []
        # for i in nums:
        #     if (len(arr) >= k):
        #         heapq.heappushpop(arr,i)
        #     else:
        #         heapq.heappush(arr,i)
        # return heapq.heappop(arr)