class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two Pointer      
        # Space Complexity: 0(N)
        lastNonZeroSpace = 0
        for i in range(len(nums)):
            print(nums, lastNonZeroSpace, i)
            if nums[i] != 0:
                nums[lastNonZeroSpace] = nums[i]
                lastNonZeroSpace += 1
        
        for i in range(lastNonZeroSpace, len(nums)):
            nums[i] = 0
        
# Space Complexity: 0(N)
#         ans = []
#         zeroCount = 0
#         for num in nums:
#             if num != 0:
#                 ans.append(num)
#             else:
#                 zeroCount += 1
#         for _ in range(zeroCount):
#             ans.append(0)
        
#         for i in range(len(nums)):
#             nums[i] = ans[i]
        
# self-help solution (TEL)        
#         start = 0
#         for i, ele in enumerate(nums):
#             if ele != 0:
#                 for j in range(i, start, -1):
#                     print(i, start, j)
#                     print(nums)
#                     nums[j], nums[j-1] = nums[j-1], nums[j]
#                 start += 1
        
#         return nums