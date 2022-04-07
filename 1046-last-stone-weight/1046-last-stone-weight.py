class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h)> 1 and h[0]!=0:
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            heapq.heappush(h,x-y)
        return -h[0]