class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        currentlen = 0
        indHash = {}
        leftside = -1
        ls = len(s)
        for ind, ch in enumerate(s):
            if (ch in indHash) and (leftside < indHash[ch]):
                leftside = indHash[ch];
            currentlen = ind - leftside;
            if currentlen > maxlen:
                maxlen = currentlen
            indHash[ch] = ind
        currentlen = ls - leftside - 1
        if currentlen > maxlen:
            maxlen = currentlen
        return maxlen