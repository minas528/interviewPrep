class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(path, cur_sum):
            if len(path) == k:
                if cur_sum == n: res.append(path)
                return
            start = 0 if len(path) == 0 else path[-1] 
            for num in range(start + 1, 10):
                backtrack(path + [num], cur_sum + num)
        res = []
        backtrack([], 0)
        return res