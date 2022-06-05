class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        N = len(image)
        M = len(image[0])
        color = image[sr][sc]
        if image[sr][sc] == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if  0 <= r-1:
                    dfs(r-1, c)
                if 0 <= c-1:
                    dfs(r, c-1)
                if r+1 < N:
                    dfs(r+1, c)
                if c+1 < M:
                    dfs(r, c+1)
        
        dfs(sr,sc)
        return image