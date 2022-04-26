class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]
        in_mst = [False] * n
        
        mst_cost = 0
        edges_used = 0
        
        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)
            if in_mst[curr_node]:
                continue
            
            in_mst[curr_node] = True
            mst_cost += weight
            edges_used += 1
            
            for next_node in range(n):
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) +\
                                  abs(points[curr_node][1] - points[next_node][1])
                    
                    heapq.heappush(heap, (next_weight, next_node))
                    
        return mst_cost