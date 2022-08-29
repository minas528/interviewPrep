class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            grid[x][y] = "0"
            # print(grid)
            for i, j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=i<len(grid) and 0<= j<len(grid[0]) and grid[i][j]=="1":
                    dfs(grid,i,j)
                  
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # print('h',grid[i][j])
                    dfs(grid,i,j)
                    islands += 1
        return islands