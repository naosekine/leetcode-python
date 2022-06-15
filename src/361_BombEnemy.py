class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_count = 0
        rows_count = 0
        cols_count = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if col == 0 or grid[row][col-1] == 'W':
                    rows_count = 0
                    for c in range(col, cols):
                        if grid[row][c] == 'E':
                            rows_count += 1
                        elif grid[row][c] == 'W':
                            break

                if row == 0 or grid[row-1][col] == 'W':
                    cols_count[col] = 0
                    for r in range(row, rows):
                        if grid[r][col] == 'E':
                            cols_count[col] += 1
                        elif grid[r][col] == 'W':
                            break
                
                if grid[row][col] == '0':
                    curr_count = rows_count + cols_count[col]
                    max_count = max(curr_count, max_count)
        return max_count