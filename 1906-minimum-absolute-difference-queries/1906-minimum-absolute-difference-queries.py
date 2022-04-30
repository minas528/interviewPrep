class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        loc = {}
        for i, x in enumerate(nums): loc.setdefault(x, []).append(i)
        keys = sorted(loc)
        
        ans = []
        for l, r in queries: 
            prev, val = 0, inf
            for x in keys: 
                i = bisect_left(loc[x], l)
                if i < len(loc[x]) and loc[x][i] <= r: 
                    if prev: val = min(val, x - prev)
                    prev = x 
            ans.append(val if val < inf else -1)
        return ans