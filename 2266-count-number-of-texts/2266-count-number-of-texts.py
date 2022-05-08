class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        
        MOD = 10**9 + 7
        stack = []
        count = []
        res = 1
        for char in pressedKeys:
            if stack and stack[-1] == char:
                if not count:
                    count.append(1)
                elif char in '79' and len(count)<4:
                    count.append(count[-1]*2)
                elif len(count)<3:
                    count.append(count[-1]*2)
                else:
                    count.append(sum(count))
                    count.pop(0)
            else:
                if count and count[-1]>1:
                    res = (res*count[-1])%MOD
                count = [1]
                stack.append(char)
        return (res*count[-1])%MOD 