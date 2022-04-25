class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        '''
        count_left
        count_right
        
        (n- count_left- count_right -1) * count_left * count_right
        '''
        adj = defaultdict(list)
        for index, p in enumerate(parents):
            adj[p].append(index)
        n = len(parents)
        print(adj)
        def dfs(cur, arr):
            left = [0,0]
            if cur not in adj:
                arr.append(n-1)
                return 1
            for i, nbr in enumerate(adj[cur]):
                left[i] = dfs(nbr, arr)
            if  left[0] and  left[1]:
                print(f'here {cur}')
                if n-1-left[0]-left[1]:
                    arr.append((n-1-left[0]-left[1])*left[0]*left[1])
                else:
                    arr.append(left[0]*left[1])
            elif  left[0]:
                if (n-1-left[0]-left[1]):
                    arr.append((n-1-left[0])*left[0])
                else:
                    arr.append(left[0])
            elif  left[1]:
                if (n-1-left[0]-left[1]):
                    arr.append((n-1-left[1])*left[1])
                else:
                    arr.append(left[0])
            return 1 + sum(left)
        arr = []
        dfs(0, arr)
        return Counter(arr)[max(arr)]
            