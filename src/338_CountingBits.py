class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1) 
        return ans        
        
        # ans = []
        # for i in range(n+1):
        #     j = bin(i)[2:].count('1')
        #     ans.append(j)
        # return ans