'''
    https://leetcode.com/problems/partition-labels/submissions/
    763. Partition Labels
    
    A string S of lowercase English letters is given. We want to 
    partition this string into as many parts as possible so that 
    each letter appears in at most one part, and return a list of 
    integers representing the size of these parts.

 
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rrrr = {}
        for s in range(len(S)):
            if S[s] in rrrr:
                if len(rrrr[S[s]]) ==1:
                    rrrr[S[s]].append(s)
                else:
                    rrrr[S[s]][1]=s
            else:
                rrrr[S[s]] = [s]
        c= []
        for _, lst in rrrr.items():
            if len(lst)==1:
                lst.append(lst[0])
                c.append(lst)
            else:
                c.append(lst)
        # print(c)
        l =len(c)
        
        i = 1
        while True:
            if c[i][0]<c[i-1][1]:
                c[i-1][1] = max(c[i][1],c[i-1][1])
                c.pop(i)
            else: i+=1
            if len(c) == i:
                break
        # print(c)
        res =[]
        for i in c:
            res.append(i[1]-i[0]+1)
        return res