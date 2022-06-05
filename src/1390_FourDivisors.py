import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            count = 0
            numsum = 0
            for i in range(1, int(math.sqrt(num)+1)):
                print(i)
                if num % i == 0:
                    if (num/i) == i:
                        count += 1
                        numsum += i
                    else:
                        count += 2
                        numsum += i
                        numsum += num//i
                
                if count > 4:
                    break
            if count == 4:
                answer += numsum
        return answer
                    
                    
        
#         memo = {}
#         answer = 0
#         for num in nums:
#             i = 1
#             count = 0
#             numsum = 0
#             if num in memo:
#                 if memo[num]:
#                     answer += memo[num]
#                     continue
#                 else:
#                     continue
                    
#             divisors = {}       
#             while i <= int(math.sqrt(num)):
#                 if i not in divisors:
#                     if num % i == 0:
#                         count += 1
#                         numsum += i
#                         divisors[i] = True
#                         if i < num//i:
#                             count += 1
#                             numsum += num//i
#                             divisors[num//i] = True
#                 if count > 4:
#                     memo[num] = False
#                     break
#                 i += 1
#             print(divisors)
#             if count == 4:
#                 memo[num] = numsum
#                 answer += numsum
                
#         return answer
                    