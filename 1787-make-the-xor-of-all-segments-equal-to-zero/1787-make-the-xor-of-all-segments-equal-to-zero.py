class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        freq = [defaultdict(int) for _ in range(k)]
        for i,num in enumerate(nums):
            freq[i%k][num] += 1

        max_save = []
        for i in range(k):
            max_save.append(max(freq[i].values()))

        max_save_suffix = max_save[::]
        for i in range(k-2,-1,-1):
            max_save_suffix[i] += max_save_suffix[i+1]
        self.save = max_save_suffix[0] - min(max_save)
        def DFS(i,state,cur_save):
            if i == k:
                if state == 0:
                    self.save = max(self.save,cur_save)
            else:
                if cur_save + max_save_suffix[i] > self.save:  ### pruning
                    for num in freq[i]:
                        DFS(i+1,state^num,cur_save+freq[i][num])
                      
        DFS(0,0,0)
        return len(nums)-self.save 