'''
    https://leetcode.com/contest/weekly-contest-184/problems/string-matching-in-an-array/
    1408. String Matching in an Array
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[j].find(words[i]) !=-1:#in words[i] and len(words[j]) >= len(words[i]):
                    # print(words[i],words[j])
                    res.append(words[i])
                    break
        return res