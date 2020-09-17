'''
    https://leetcode.com/problems/sort-an-array/submissions/
    912. Sort an Array

    Given an array of integers nums, sort the array in ascending order.

        Example 1:

        Input: nums = [5,2,3,1]
        Output: [1,2,3,5]
        Example 2:

        Input: nums = [5,1,1,2,0,0]
        Output: [0,0,1,1,2,5]
        

        Constraints:

        1 <= nums.length <= 50000
        -50000 <= nums[i] <= 50000
'''

##  Sol - one QuickSort

class Solution:
    def sortArray(self, nums) :
        def QuickSort(nums, start, end):
            if start >= end:
                return
            i, j = start+1, end
            while i <= j:
                while i <= j and nums[i] <= nums[start]:
                    i += 1
                while i <= j and nums[j] >= nums[start]:    
                    j-=1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            nums[start], nums[j] = nums[j], nums[start]
            QuickSort(nums,start,j-1)
            QuickSort(nums, j+1, end)
        QuickSort(nums,0, len(nums)-1)            
        return nums


## Sol 2 = MergeSort
def MergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])

    sol = merge(left, right)
    return sol

def merge(left, right):
    i = j = 0
    result = []
    while i <len(left) and j <len(right):
        if left[i]<= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    arr = [29, 64, 73, 34, 20]
    arr2 = [7, 5, 2, 4, 3, 9]
    res = MergeSort(arr2)
    print(res)


