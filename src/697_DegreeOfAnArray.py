from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = {}, {}
        count = defaultdict(int)
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
        
        max_count = max(count.values())
        minlength = len(nums)
        for num in nums:
            if count[num] == max_count:
                length =  right[num] - left[num] + 1
                minlength = min(minlength, length)
        return minlength
        
        
# self-help solution
#         numC = Counter(nums)
#         #出現回数多い順リスト
#         maxzyun = numC.most_common()
#         # print(maxzyun)
#         max_num= maxzyun[0][1]
#         max_key = []
#         for k, v in maxzyun:
#             if v == max_num:
#                 max_key.append(k)
#         # print(max_key)
#         minlen = math.inf
#         for k in max_key:
#             count = 0
#             start = 0
#             for i, num in enumerate(nums):
#                 if num == k:
#                     if count == 0:
#                         start = i
#                     count += 1
#                     if count == max_num:
#                         curlen = i - start + 1
#                         minlen = min(minlen, curlen)
#         return minlen
        
