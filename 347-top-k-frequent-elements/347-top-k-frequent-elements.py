class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorte_d = Counter(nums)
        print(sorte_d)
        sorte_d = sorted(sorte_d.items(), key=lambda x:(x[1], x[0]), reverse = True)
        return [key for key, value in sorte_d[:k]]