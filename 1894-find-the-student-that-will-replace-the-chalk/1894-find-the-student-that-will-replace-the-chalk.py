class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        if k>=s: k=k%s
        for i,v in enumerate(chalk):
            if k-v == 0: return i+1
            elif k-v < 0: return i
            else: k = k - v