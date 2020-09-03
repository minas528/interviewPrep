'''
    https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
    1351. Count Negative Numbers in a Sorted Matrix
    Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

    Return the number of negative numbers in grid.

 

        Example 1:

        Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        Output: 8
        Explanation: There are 8 negatives number in the matrix.
        Example 2:

        Input: grid = [[3,2],[1,0]]
        Output: 0
        Example 3:

        Input: grid = [[1,-1],[-1,-1]]
        Output: 3
        Example 4:

        Input: grid = [[-1]]
        Output: 1
        

        Constraints:

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 100
        -100 <= grid[i][j] <= 100
'''
# Solution One bruet force
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j] <0:
                    counter += 1
                else:
                    break
        return counter



#Solution Tw0 O(mlog(n))
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
                start, end = 0, len(row)
                while start<end:
                    mid = start +(end -start) // 2
                    if row[mid]<0:
                        end = mid
                    else:
                        start = mid+1
                return len(row)- start

        count = 0
        for row in grid:
            count += bin(row)
            return(count)