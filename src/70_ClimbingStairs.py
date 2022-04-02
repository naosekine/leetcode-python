class Solution:
    def climbStairs(self, n) -> int:
        def dfs(k):
            if k not in dic:
                dic[k] = dfs(k-1) + dfs(k-2)
            return dic[k]
                
        dic = {1:1, 2:2}
        return dfs(n)
  
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(45))    