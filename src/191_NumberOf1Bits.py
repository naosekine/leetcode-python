class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = list(bin(n)[2:])
        if n < 0:
            if len(bin) < 32:
                return bin_n.count('1') + 32 - len(bin)
        else:
            return bin_n.count('1')        