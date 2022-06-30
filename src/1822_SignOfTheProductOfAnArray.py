class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_count = 0
        for ele in nums:
            if ele == 0:
                return 0
            elif ele < 0:
                negative_count += 1
        if negative_count % 2 == 0:
            return 1
        else:
            return -1
                
#         ans = 1
#         for ele in nums:
#             ans *= ele
        
#         if ans > 0:
#             return 1
#         elif ans < 0:
#             return -1
#         else:
#             return 0
            