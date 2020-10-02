"""
    https://leetcode.com/problems/clone-graph/
    133. Clone Graph
"""


import collections
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None
        visited = set()
        que = collections.deque()
        que.append(node)
        adjList = {}
        while que:
            curr = que.popleft()
            temp = []
            for nex in curr.neighbors:
                if nex not in visited:
                    que.append(nex)
                temp.append(nex.val)
            visited.add(curr)
            adjList[curr.val] = temp
        build = {}
        for nod, neighbor in adjList.items():
            if nod not in build:
                n = Node(nod)
                build[nod] = n
            for el in neighbor:
                if el not in build:
                    n = Node(el)
                    build[el] = n
                build[nod].neighbors.append(build[el])
        return build[1]
                 
            