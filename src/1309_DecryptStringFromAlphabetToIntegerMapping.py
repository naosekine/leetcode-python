class Solution:
    def freqAlphabets(self, s: str) -> str:
        list_s = list(s)
        nums = []
        while list_s:
            cha = list_s.pop()
            if cha == '#':
                a = list_s.pop()
                b = list_s.pop()
                nums.append(int(b + a))
            else:
                nums.append(int(cha))
        nums = nums[::-1]

        ans = ''
        for num in nums:
            alp = chr(ord('a') + num-1)
            ans += alp
        return ans