class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n-1) == 0

        # another solution
        # if n == 0:
        #     return False
        # while n % 2 == 0:
        #     n /= 2
        # return n == 1
        
        # self-help solution
        # bin_n = bin(n)[2:]
        # if bin_n[0] == '1':
        #     for bit in bin_n[1:]:
        #         if bit != '0':
        #             return False
        #     return True
        # return False