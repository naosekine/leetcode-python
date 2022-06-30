class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sort_w = []
        if not self.sort_w:
            tmp = 0
            for i in range(len(self.w)):
                tmp += self.w[i]
                self.sort_w.append(tmp)

    def pickIndex(self) -> int:
        n = random.randint(1, sum(self.w))
        # print(self.sort_w)
        left = 0
        right = len(self.w)-1
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid , right, n)
            if 0 < mid:
                if self.sort_w[mid-1] < n <= self.sort_w[mid]:
                    return mid
                if self.sort_w[mid] < n:
                    left = mid+1
                if n <= self.sort_w[mid-1]:
                    right = mid-1
            else:
                if 0 < n <= self.sort_w[mid]:
                    return 0
                else:
                    left = mid + 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()