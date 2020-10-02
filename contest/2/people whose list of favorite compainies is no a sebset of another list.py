'''
    https://leetcode.com/contest/weekly-contest-189/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
    1452. People Whose List of Favorite Companies Is Not a Subset of Another List
'''

from collections import defaultdict
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ddd = {}
        for i in range(len(favoriteCompanies)):
            ddd[i] = set(favoriteCompanies[i])
        res = []
        for i, j in ddd.items():
            stat = False
            for f, k in ddd.items():
                
                if  j.issubset(k) and f != i:
                    stat = True
                    break
            if stat == False:
                res.append(i)
        return res