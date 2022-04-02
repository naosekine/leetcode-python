class Solution:
    def fib(self, n: int) -> int:
        # DFS
        def dfs(k):
            if k not in dic:
                dic[k] = dfs(k-1) + dfs(k-2)
            return dic[k]

        dic = {0:0, 1:1}        
        return dfs(n)
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))
    print(s.fib(30))
