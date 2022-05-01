class Solution:
    def sortedSquares(self, nums):
        answer = []
        i = 0
        j = len(nums) -1
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                answer.append(nums[j]**2)
                j -= 1
            else:
                answer.append(nums[i]**2)
                i += 1
        return answer[::-1]