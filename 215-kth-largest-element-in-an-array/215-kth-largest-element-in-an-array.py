import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):
        #     nums[i] = -nums[i]
        # heapq.heapify(nums)
        # for i in range(k):
        #     res = heapq.heappop(nums)
        # return -res
        arr = []
        for i in nums:
            if (len(arr) >= k):
                heapq.heappushpop(arr,i)
            else:
                heapq.heappush(arr,i)
        return heapq.heappop(arr)