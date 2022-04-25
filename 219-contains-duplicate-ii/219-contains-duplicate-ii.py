class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        look = set()
        for index, num in enumerate(nums):
            if num in look:
                return True
            look.add(num)
            if len(look) >k:
                look.remove(nums[index-k])
        return False