'''
    https://leetcode.com/problems/pascals-triangle/
    118. Pascal's Triangle
    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Example:

    Input: 5
    Output:
    [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1]
    ]
'''


class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        else:
            res = [[1]]
            for i in range(numRows -1):
                temp = [1]
                for j in range(i):
                    temp.append(res[-1][j] + res[-1][j+1])
                temp.append(1)
                res.append(temp)
                
        return res

if __name__ == '__main__':
    solution = Solution()
    test = solution.generate(5)
    print(test)