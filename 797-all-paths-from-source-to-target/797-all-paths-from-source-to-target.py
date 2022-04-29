class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(curr, last, path, res):
            for node in graph[curr]:
                if node == last:
                    path.append(node)
                    res.append(path[:])
                else:
                    path.append(node)
                    dfs(node, last, path, res)
                if path:
                    path.pop()
        dfs(0, len(graph) -1, [0], res)
        return res