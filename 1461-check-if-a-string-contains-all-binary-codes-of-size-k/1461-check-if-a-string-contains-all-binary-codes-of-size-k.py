class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        last = int(s[:k], 2)
        ss = {last}
        for i in range(k, len(s)):
            last = last*2 - (int(s[i-k])<<k)  + int(s[i])
            ss.add(last)
        
        return len(ss) == 1<<k