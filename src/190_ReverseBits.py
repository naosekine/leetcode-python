class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = list(bin(n)[2:])
        bin_n = bin_n[::-1]
        if 0 <= n:
            for _ in range(32 - len(bin_n)):
                bin_n.append('0')
        else:
            for _ in range(32 - len(bin_n)):
                bin_n.append('1')
        
        return int(''.join(bin_n), 2)
            
            