class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        count = 0
        def checkPalindrom(string,i,j):
            nonlocal count
            while i>=0 and j<len(string) and string[i] == string[j]:
                count +=1
                i-=1
                j+=1
        for i in range(len(s)):
            checkPalindrom(s,i,i)
            checkPalindrom(s,i,i+1)
            
        return count