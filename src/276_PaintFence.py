class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if k == 1 and n > 2:
            return 0
        elif k == 1:
            return 1
        dp = [0] * n
        dp[0] = k
        dp[1] = k*k
        for i in range(2, n):
            dp[i] = dp[i-1]*k - (dp[i-1]-dp[i-2]*(k-1))
        
        return dp[-1]