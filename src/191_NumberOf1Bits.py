class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1
        return ans

        # bin_n = list(bin(n)[2:])
        # if n < 0:
        #     if len(bin) < 32:
        #         return bin_n.count('1') + 32 - len(bin)
        # else:
        #     return bin_n.count('1')        