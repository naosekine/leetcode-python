class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid[0])):
            if i == 0 and obstacleGrid[0][0] == 0:
                dp[0][i] = 1
            elif obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
                
        for i in range(len(obstacleGrid)):
            dp[i][0] = 1
            if i == 0 and obstacleGrid[0][0] == 0:
                dp[i][0] = 1
            elif obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]        
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i-1][j] != 1 and obstacleGrid[i][j-1] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif obstacleGrid[i-1][j] != 1:
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i][j-1] != 1:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[-1][-1]