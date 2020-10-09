'''
    https://leetcode.com/contest/weekly-contest-209/problems/special-array-with-x-elements-greater-than-or-equal-x/
    1608. Special Array With X Elements Greater Than or Equal X
    Dificulty = East
'''
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ter = {}
        for i in range(len(nums)+1):
            ter[i] = 0
        
        for i in range(len(nums)):
            # print(min(nums[i]+1,len(nums)+1))
            for j in range(min(nums[i]+1,len(nums)+1)):
                ter[j] +=1
        for x,y in ter.items():
            if x==y:
                return x
        return -1