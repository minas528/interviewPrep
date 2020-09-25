'''
    https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
    1443. Minimum Time to Collect All Apples in a Tree
'''



class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def do_dfs(node):
            time = 0
            stack.add(node)
            for adj in adjList[node]:
                if adj not in stack : 
                    adjTime = dfs(adj)
                    if hasApple[adj] or adjTime:
                        time += adjTime + 2
            return time
        
        adjList = [[] for _ in range(n)]  
        for node,child in edges:
            adjList[node].append(child)
            adjList[child].append(node)
            
        stack = set()
        def dfs(node):
            time = 0
            stack.add(node)
            for adj in adjList[node]:
                if adj not in stack : 
                    adjTime = dfs(adj)
                    if hasApple[adj] or adjTime:
                        time += adjTime + 2
            return time
        res = do_dfs(0)
        return res