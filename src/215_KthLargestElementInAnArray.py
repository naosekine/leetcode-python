from collections import defaultdict
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        min_num = min(nums)
        backet = defaultdict(int)
        for num in nums:
            backet[num] += 1
        
        sorted_nums = []
        for i in range(min_num, max_num+1):
            if backet[i]>0:
                for _ in range(backet[i]):
                    sorted_nums.append(i)
        return sorted_nums[-k]