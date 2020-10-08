'''
    https://leetcode.com/problems/shortest-bridge/submissions/
    934. Shortest Bridge

    In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

    Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

    Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

    

    Example 1:

    Input: A = [[0,1],[1,0]]
    Output: 1
    Example 2:

    Input: A = [[0,1,0],[0,0,0],[0,0,1]]
    Output: 2
    Example 3:

    Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Output: 1
'''

import collections
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        visited = set()
        
        def do_dfs(A,i,j,visited,seen):
            visited.add((i,j))
            seen.add((i,j))
            for x,y in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
                if 0<= x < len(A) and 0<= y<len(A[0]) and A[x][y] and (x,y) not in visited:
                    do_dfs(A,x,y,visited,seen)
            # return seen
        
        comp = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and (i,j) not in visited:
                    seen = set()
                    do_dfs(A, i,j, visited,seen)
                    # print(a)
                    comp.append(seen)
                
        s,t = comp[0],comp[1]
        # print(comp,len(comp))
        queue = collections.deque([(node,0) for node in s])
        done = s
        while queue:
            
            node, d = queue.popleft()
            if node in t:return d-1
            # print('here',node)
            for n in[(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]:
                # print(n,A[n[0]][n[1]] , n not in done)
                if 0<= n[0] < len(A) and 0<= n[1]<len(A[0]) and n not in done:
                    # print('here')
                    queue.append((n,d+1))
                    done.add(n)

        
                    