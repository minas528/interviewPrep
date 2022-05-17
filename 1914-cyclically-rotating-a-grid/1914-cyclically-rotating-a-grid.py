class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid);
        cols = len(grid[0]);

        for layer in range(min(rows, cols) // 2):
            r, c = layer, layer;

            layer_perimeter = (rows - layer * 2) * 2 + (cols - (layer + 1) * 2) * 2
            rotations = k % layer_perimeter;

            for _ in range(rotations):
                prev = grid[r][c]
                for i in range(r + 1, rows - r - 1): grid[i][c], prev = prev, grid[i][c];
                for i in range(c, cols - c): grid[rows - r - 1][i], prev = prev, grid[rows - r - 1][i];
                for i in range(rows - r - 2, r - 1, -1): grid[i][cols - c - 1], prev = prev, grid[i][cols - c - 1];
                for i in range(cols - c - 2, c - 1, -1): grid[r][i], prev = prev, grid[r][i]

        return grid;