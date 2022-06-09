class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(1,len(numbers)+1):
            if numbers[i-1] in dict:
                return [dict[numbers[i-1]],i]
            else:
                dict[target - numbers[i-1]] = i