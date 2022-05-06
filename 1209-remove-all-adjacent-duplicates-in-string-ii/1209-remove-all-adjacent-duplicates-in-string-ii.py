class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] % k == 0:
                    stack.pop()
            else:
                stack.append([c, 1])
        
        return "".join([c*f for c, f in stack if f%k])