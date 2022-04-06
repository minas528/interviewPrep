class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        for i, x in enumerate(A):
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                elif A[j] != A[k]: # We have A[j] + A[k] == T.
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return int(ans)