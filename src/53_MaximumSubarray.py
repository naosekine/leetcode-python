class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0]*len(nums)
        for i,num in enumerate(nums):
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))          