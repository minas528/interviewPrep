class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic={}
        for w in words:
            if w in dic:
                dic[w]+=1
            else:
                dic[w]=1
        res=0    
        for key,value in dic.items():
            st=key
            n=len(st)
            i,j=0,0
            while i<n and j<len(s):
                if st[i]==s[j]:
                    i+=1
                j+=1
            if i==n:
                res+=value
        return res