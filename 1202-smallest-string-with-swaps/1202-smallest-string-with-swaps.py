class UnionFind:
    def __init__(self,n:int):
        self.rank = [1]*n
        self.root =[ 1*i for i in range(n)]
       
    def find(self,x:int):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x] 
    def union(self,x:int,y:int):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] >self.rank[rootY]:
                self.root[rootY] = rootX
            if self.rank[rootX] <self.rank[rootY]:
                self.root[rootX] = rootY
            if self.rank[rootX] == self.rank[rootY]:
                self.root[rootX] = rootY
                self.rank[rootY]  += 1
    def isConnect(self,x:int,y:int):
        return self.find(x) == self.find(y)
                    
                
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        myUF = UnionFind(len(s))
        res = [""]*len(s)
        Dict = defaultdict(list)
        for curpair in pairs:  
            a,b = curpair[0],curpair[1]
            myUF.union(a,b)
        
        for i in range(len(s)):
            root = myUF.find(i)
            Dict[root].append(i)
        for key in Dict:
            items = Dict[key]
            subs = [s[i] for i in items]
            
            subs = sorted(subs)
            items = sorted(items)
            for i in range(len(items)):
                res[items[i]] = subs[i]            
        return "".join(res)
