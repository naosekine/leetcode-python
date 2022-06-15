class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(n) for n in num]
        nums = int(''.join(num))
        ans = nums + k
        return list(str(ans))