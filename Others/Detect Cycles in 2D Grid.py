class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        row, col = len(grid), len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited:
                    found_cycle = self.do_dfs(grid, None,None, i, j, row, col, visited)
                    if found_cycle:
                        return found_cycle
        return False
    
    def do_dfs(self, grid, parent_x, parent_y, x, y,row, col, visited):
            if (x,y)  in visited:
                return True
            
            visited.add((x, y))
            nighbors = self.get_nighbors(x,y, row, col)
            found = False
            for new_x,new_y in nighbors:
                if (parent_x!= new_x or parent_y!= new_y) and (grid[ new_x][new_y]== grid[x][y]):
                    found = found or self.do_dfs(grid, x,y, new_x, new_y, row, col, visited)
            return found
        
    def get_nighbors(self, i,j, row, col):
            neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            valid = []
            for x,y in neighbours:
                if 0<=x<row and 0<=y< col:
                    valid.append((x,y))
            return valid
            
