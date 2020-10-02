'''
    https://leetcode.com/contest/weekly-contest-184/problems/queries-on-a-permutation-with-key/
    1409. Queries on a Permutation With Key
'''

import collections
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        for i in range(m):
            p.append(i+1)
        # print(p)
        res = []
        for el in queries:
            inx = p.index(el)
            res.append(inx)
            a = p.pop(inx)
            p.insert(0,a)
            # print(p)
        return res

