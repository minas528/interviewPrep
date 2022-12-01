class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        d = 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        res = 0
        for i,c in enumerate(s):
            if len(s)//2 == i:
                d = -1
            if c in vowels:
                res += d
        return res == 0