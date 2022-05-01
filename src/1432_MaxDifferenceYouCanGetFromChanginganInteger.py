class Solution:
    def maxDiff(self, num: int) -> int:
        strnum = str(num)
        max_num = 0
        min_num = 1000000000
        for digit in strnum:
            for y in range(10):
                new_strnum = strnum.replace(digit, str(y))
                new_num = int(new_strnum)
                if new_strnum[0] != '0':
                    if new_num < min_num:
                        min_num = new_num
                    if new_num > max_num:
                        max_num = new_num
                    
        return max_num - min_num
