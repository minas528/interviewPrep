'''
https://leetcode.com/problems/subarrays-with-k-different-integers/submissions/
992. Subarrays with K Different Integers
Difficulty: Hard
'''

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        return (self.atMostK(A, len(A), K) 
                - self.atMostK(A, len(A), K - 1))
    
    def atMostK(self, arr, n, k):
        count = 0
        left = 0
        right = 0

        cache_map = {}

        while(right < n):

            if arr[right] not in cache_map:
                cache_map[arr[right]] = 0

            cache_map[arr[right]] += 1

            while(len(cache_map) > k):

                if arr[left] not in cache_map:
                    cache_map[arr[left]] = 0

                cache_map[arr[left]] -= 1

                if cache_map[arr[left]] == 0:
                    del cache_map[arr[left]]

                left += 1

            count += right - left + 1
            right += 1

        return count
