class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        d = []
        K = len(nums)
        count = collections.defaultdict(int)
        for i, num in enumerate(nums):
            for n in num:
                d.append([n, i])
        d.sort(key=lambda x: x[0])
        res = []
        left = 0
        for right, n in enumerate(d):
            count[n[1]] += 1
            while len(count)==K:
                if not res or d[right][0]-d[left][0]<res[1]-res[0]:
                    res = [d[left][0], d[right][0]]
                count[d[left][1]] -= 1
                if count[d[left][1]]==0:
                    count.pop(d[left][1])
                left += 1
        return res