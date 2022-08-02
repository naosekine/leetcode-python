class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                print(i, j)
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
        # stack = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i]>stack[-1]:
        #         stack.append(nums[i])
        #     else:
        #         j = 0
        #         while nums[i] > stack[j]:
        #             j += 1
        #         stack[j] = nums[i]            
        # return len(stack)