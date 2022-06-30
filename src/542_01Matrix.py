from collections import deque
import sys
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
# DP
        rows = len(mat)
        cols = len(mat[0])
        INF = rows + cols
        dist = [[INF for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j]+ 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1]+ 1)
                        
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i < rows-1:
                        dist[i][j] = min(dist[i][j], dist[i+1][j]+ 1)
                    if j < cols-1:
                        dist[i][j] = min(dist[i][j], dist[i][j+1]+ 1)
        
                    
        return dist
        
# BFS        
#         rows = len(mat)
#         cols = len(mat[0])
#         INF = rows + cols
#         dist = [[INF for _ in range(cols)] for _ in range(rows)]
#         queue = deque()
#         for r in range(rows):
#             for c in range(cols):
#                 if mat[r][c] == 0:
#                     dist[r][c] = 0
#                     queue.append((r,c))
        
#         four_dire = [(-1,0),(1,0),(0,-1),(0,1),]
        
#         while queue:
#             r, c = queue.popleft()
            
#             for x, y in four_dire:
#                 if 0 <= r+x <= rows-1 and 0 <= c+y <= cols-1:
#                     if dist[r+x][c+y] > dist[r][c] + 1:
#                         dist[r+x][c+y] = dist[r][c] + 1
#                         queue.append((r+x, c+y))
        
#         return dist
