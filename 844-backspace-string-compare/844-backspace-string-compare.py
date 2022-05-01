class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for c in s:
            if c == '#':
                if s1:
                    s1.pop()
            else:
                s1.append(c)
        for c in t:
            if c == '#':
                if t1:
                    t1.pop()
            else:
                t1.append(c)
        print(s1, t1)
        return s1==t1