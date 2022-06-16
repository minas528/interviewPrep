class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1: return ''
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            len_ = max((len1, len2))
            if(len_> end - start):
                start = i - (len_ -1)//2
                end = i+ len_//2
        return s[start:end+1]
    def expandAroundCenter(self, s, left, right):
        l = left
        r = right
        while l>= 0 and r <len(s) and s[l]== s[r]:
            l-=1
            r+=1
        return r-l-1;