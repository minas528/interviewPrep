class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] != 0 or grid[-1][-1] !=0:
            return -1
        Q = collections.deque()
        Q.append((0,0, 1))
        seen = set((0,0))
        while Q:
            i,j, d = Q.popleft()
            if (i , j) ==(len(grid) -1 , len(grid[0])-1):
                return d
            nbrs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for nbr in nbrs:
                x = i+ nbr[0]
                y = j + nbr[1]
                if 0<= x <len(grid) and 0<=y< len(grid[0]) and (x,y) not in seen and grid[x][y] == 0:
                    seen.add((x,y))
                    Q.append((x,y,d+1))
        return -1

        