class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder = []
        for i in range(1, len(heights)):
            # print(ladder)
            if heights[i] > heights[i-1]:
                heapq.heappush(ladder, heights[i] - heights[i-1])
            if len(ladder) > ladders:
                bricks -= heapq.heappop(ladder)
            if bricks < 0:
                return i-1
        return len(heights) - 1