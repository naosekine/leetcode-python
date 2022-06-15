from collections import deque
import sys
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat
        
        cols = len(mat[0])
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        print(dist)
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        
        udlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            curr = queue.popleft()
            
            for i in range(4):
                new_r = curr[0] + udlr[i][0]
                new_c = curr[1] + udlr[i][1]
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if dist[new_r][new_c] > dist[curr[0]][curr[1]] + 1:
                        dist[new_r][new_c] = dist[curr[0]][curr[1]] + 1
                        queue.append((new_r, new_c))
            
        return dist
        