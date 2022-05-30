class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_k = 2 ** maximumBit
        n = len(nums)
        answer = []
        while nums:
            if len(nums) == n:
                xor = nums[0]
                for i in range(len(nums)):
                    if i > 0:
                        xor = xor ^ nums[i]
            else:
                xor = xor ^ last_elm
            k = ''
            for i in bin(xor)[2:]:
                if i == '0':
                    k += '1'
                else:
                    k += '0'
                    
            if len(k) > maximumBit:
                k = k[len(k)-maximumBit:]
            elif len(k) < maximumBit:
                for _ in range(maximumBit-len(k)):
                    k = '1' + k

            answer.append(int(k, 2))
            last_elm = nums.pop()
    
        return answer