class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        per = len(arr)//4
        for num in arr:
            c = arr.count(num)
            if c > per:
                return num
            
