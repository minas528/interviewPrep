'''
    https://leetcode.com/problems/count-servers-that-communicate/submissions/


    You are given a map of a server center, represented as a m * n integer matrix grid, 
    where 1 means that on that cell there is a server and 0 means that it is no server.
    Two servers are said to communicate if they are on the same row or on the same column.

    Return the number of servers that communicate with any other server.
'''


class Solution:
    def countServers(self, grid) -> int:
        row_map = {}
        col_map = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i not in row_map:
                        row_map[i] = 1
                    else:
                        row_map[i] +=1
                    if j not in col_map:
                        col_map[j] = 1
                    else:
                        col_map[j] +=1
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (row_map[i]>1 or col_map[j]>1):
                    count +=1
        return count
