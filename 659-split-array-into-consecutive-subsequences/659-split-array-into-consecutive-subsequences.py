class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        res = False
        tracker = [[nums[0]]]
        for i in range(1,len(nums)):
            added = False
            for t in tracker[::-1]:
                if t[-1] == nums[i]-1:
                    t.append(nums[i])
                    added = True
                    break
            if not added:
                tracker.append([nums[i]])
        for t in tracker:
            if len(t)<3:
                return False
        return True