'''
    https://leetcode.com/problems/search-a-2d-matrix/submissions/
    74. Search a 2D Matrix

    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    Example 1:

    Input:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 3
    Output: true
    Example 2:

    Input:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 13
    Output: false
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return 0
        left = 0
        right =len(matrix) * len(matrix[0])-1
        col = len(matrix[0])
        while left <= right :
            mid = (left + right) //2
            mid_value = matrix[mid//col][mid%col]
            print(mid//col,mid%col)
            if mid_value == target:
                return True
            elif mid_value > target:
                right = mid-1
            elif mid_value < target:
                left = mid +1
        return False