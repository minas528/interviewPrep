'''
    https://leetcode.com/problems/four-divisors/

    1390. Four Divisors
    Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

    If there is no such integer in the array, return 0.

    

    Example 1:

    Input: nums = [21,4,7]
    Output: 32
    Explanation:
    21 has 4 divisors: 1, 3, 7, 21
    4 has 3 divisors: 1, 2, 4
    7 has 2 divisors: 1, 7
    The answer is the sum of divisors of 21 only.
    

    Constraints:

        1 <= nums.length <= 10^4
        1 <= nums[i] <= 10^5
'''


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curr = nums[i]
            counter = 1
            divisors = []
            while counter <= sqrt(nums[i]) and len(divisors)<5:
                if nums[i]%counter == 0:
                    if counter not in divisors:
                        divisors.append(counter)
                    if nums[i]//counter not in divisors:
                        divisors.append(nums[i]//counter)
                counter+=1
            if len(divisors) == 4:
                res += sum(divisors)
            print(divisors)
                
        return res


if __name__ == '__main__':
    solution = Solution()
    test = solution.sumFourDivisors([21,4,7])
    print(test)