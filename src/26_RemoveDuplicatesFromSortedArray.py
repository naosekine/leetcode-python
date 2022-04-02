class Solution:
    def removeDuplicates(self, nums):
        new_idx = 1
        cur_num = nums[0]
        for idx in range(1,len(nums)):
            if cur_num != nums[idx]:
                cur_num = nums[idx]
                nums[new_idx] = nums[idx]
                new_idx += 1
        return new_idx
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))