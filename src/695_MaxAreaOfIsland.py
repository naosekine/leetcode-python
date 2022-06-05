import sys

sys.setrecursionlimit(5000)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])
                    and (x,y) not in seen and grid[x][y]):
                return 0
            seen.add((x,y))
            return (1 + dfs(x-1,y) + dfs(x+1,y) + dfs(x,y-1) + dfs(x,y+1))
        
        max_num=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_num = max(dfs(i,j),max_num)
        return max_num
    
#         m = len(grid)
#         n = len(grid[0])
#         seen = set()
#         max_cells = 0
#         for i in range(m):
#             for j in range(n):
#                 if (i,j) not in seen:
#                     island = Island(grid, seen)
#                     max_cells = max(island.dfs(i,j), max_cells)
#                     seen = island.seen
#         return max_cells

# class Island:
#         def __init__(self, grid, seen):
#             self.grid = grid
#             self.seen = seen
#             self.m = len(self.grid)
#             self.n = len(self.grid[0])
    
#         def dfs(self, x, y):
#             if not (0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])
#                     and (x, y) not in self.seen and self.grid[x][y]):
#                 return 0
#             self.seen.add((x,y))
#             return (1 + self.dfs(x-1,y)+ self.dfs(x+1,y)+ self.dfs(x,y-1)+ self.dfs(x,y+1))