class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        
        for row, col in indices:
            rows[row] += 1
            cols[col] += 1
            
        rows_count = 0
        for row in range(m):
            if rows[row]  % 2 == 1:
                rows_count += 1
        cols_count = 0
        for col in range(n):
            if cols[col] % 2 == 1:
                cols_count += 1
        return rows_count * n + cols_count * m - 2 * rows_count * cols_count
