class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        look = {}
        for index, num in enumerate(nums):
            if num in look and abs(look[num] - index) <= k: return True
            look[num] = index
        return False