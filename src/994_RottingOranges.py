from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        q = deque()
        fresh_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        #Mark the round / level, _i.e_ the ticker of timestamp
        q.append((-1, -1))
        
        minutes_elapsed = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            row, col = q.popleft()
            
            if row == -1:
                minutes_elapsed += 1
                
                if q:
                    q.append((-1,-1))
                    
            for d in directions:
                neighbor_row = row + d[0]
                neighbor_col = col + d[1]
                
                if 0 <= neighbor_row < rows and 0<= neighbor_col < cols:
                    if grid[neighbor_row][neighbor_col] == 1:
                        grid[neighbor_row][neighbor_col] = 2
                        fresh_oranges -= 1
                        q.append((neighbor_row, neighbor_col))    
                
        if fresh_oranges:
            return -1
        else:
            return minutes_elapsed
        
        
#         rows = len(grid)
#         cols = len(grid[0])
        
#         q = deque()
        
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == 2:
#                     q.append((i, j))
        
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         count = 0
#         while q:
#             print(q)
#             q_next = deque()
#             while q:
#                 curr = q.popleft()
#                 for i in range(4):
#                     new_r = curr[0] + directions[i][0]
#                     new_c = curr[1] + directions[i][1]
#                     if 0 <= new_r < rows and 0 <= new_c < cols:
#                         if grid[new_r][new_c] == 1:
#                             grid[new_r][new_c] = 2
#                             q_next.append((new_r, new_c))
#             q = q_next
#             if q:
#                 count += 1
        
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == 1:
#                     return -1
#         return count
                

        