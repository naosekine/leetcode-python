class Solution:
    def climbStairs(self, n) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2 , n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        # another solution
        # def dfs(k):
        #     if k not in dic:
        #         dic[k] = dfs(k-1) + dfs(k-2)
        #     return dic[k]
                
        # dic = {1:1, 2:2}
        # return dfs(n)
  
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(45))    