class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        prefix_sums = [[0 for i in range(cols+1)] for j in range(rows+1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sums[i][j] = prefix_sums[i][j-1] + prefix_sums[i-1][j] - prefix_sums[i-1][j-1] + matrix[i-1][j-1]
        for r1 in range(0, rows):
            for r2 in range(r1 + 1, rows + 1):
                hash_col_sums = defaultdict(int)
                hash_col_sums[0] = 1
                for c1 in range(1, cols + 1):
                    cur_sum = prefix_sums[r2][c1] - prefix_sums[r1][c1]
                    res += hash_col_sums[cur_sum - target]
                    hash_col_sums[cur_sum] += 1
        return res