'''
    https://leetcode.com/problems/sort-characters-by-frequency/submissions/
    451. Sort Characters By Frequency
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        fr = {}
        for i in range(len(s)):
            if s[i] in fr:
                fr[s[i]] +=1
            else:
                fr[s[i]] = 1
        sr = sorted(fr.items(), key=lambda x:x[1],reverse = True)
        res = ''
        for i, j in sr:
            ff = i*j
            # print(ff,i,j)
            res += ff
        return res