class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        def neighbours(i,j):
            return [ (i+x,j+y)  for x, y in moves if -1<i+x<m and -1<j+y<n ]
        
        dist = [ [float("inf")]*n for _ in range(m) ]
        dist[0][0] = 0
        
        import heapq
        que = [(0,0,0)]
        
        visited = [ [False]*n for _ in range(m) ]
        while que:
            d, i, j = heapq.heappop(que)
            
            if visited[i][j]:
                continue
            
            visited[i][j] = True
            dist[i][j] = d
            
            for ni,nj in neighbours(i,j):
                if dist[ni][nj] > max( d, abs(heights[i][j]-heights[ni][nj]) ):
                    dist[ni][nj] = max( d, abs(heights[i][j]-heights[ni][nj]) )
                    heapq.heappush( que, ( max( d, abs(heights[i][j]-heights[ni][nj]) ), ni, nj ) )
                    
        return dist[m-1][n-1]