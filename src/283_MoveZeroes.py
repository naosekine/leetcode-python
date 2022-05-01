class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0
        searcher = 1
        
        while searcher < len(nums) and zero_pointer < len(nums):
            print(zero_pointer, searcher)
            if nums[searcher] != 0:
                if nums[zero_pointer] == 0:
                    print("s!=0,z=0")
                    nums[zero_pointer] = nums[searcher]
                    nums[searcher] = 0
                    zero_pointer += 1
                    searcher += 1
                else:
                    print("s!=0,z!=0")
                    zero_pointer += 1
                    searcher += 1
            else:
                if nums[zero_pointer] == 0:
                    print("s=0,z=0")
                    searcher += 1
                else:
                    print("s=0,z!=0")
                    zero_pointer += 1
                    searcher += 1
