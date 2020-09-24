'''
    https://leetcode.com/problems/largest-number/
    179. Largest Number
    Given a list of non negative integers, arrange them such that they form the largest number.

    Example 1:

    Input: [10,2]
    Output: "210"
    Example 2:

    Input: [3,30,34,5,9]
    Output: "9534330"
    Note: The result may be very large, so you need to return a string instead of an integer.
'''

import functools
class Solution:
    def largestNumber(self, nums) -> str:
        def compare(num1, num2):
            num1, num2 = str(num1), str(num2)
            a,b = int(num1 + num2), int(num2 + num1)
            return 1 if a > b else -1
        nums = [str(num) for num in nums]
        nums = sorted(nums, key=functools.cmp_to_key(compare))
        res = nums[::-1]
        print(res)
        if res[0]=='0':
            return '0'
        return ''.join(res)
        
        