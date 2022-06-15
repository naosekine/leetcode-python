from collections import Counter 
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from functools import reduce
        from math import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2

# another solution
#         n = len(deck)
        
#         counts = Counter(deck)
#         for i in range(2, n+1):
#             if n % i == 0:
#                 if all(count % i == 0 for count in counts.values()):
#                     return True
#         return False

# self-help solution
#         if len(deck) == 1:
#             return False
        
#         deck_counts = Counter(deck)
#         min_count = min(deck_counts.values())
#         divisors = []
#         for i in range(2, min_count + 1):
#             if min_count % i == 0:
#                 divisors.append(i)
                
#         for divisor in divisors:
#             flag = True
#             for count in deck_counts.values():
#                 if count % divisor != 0:
#                     flag = False
#             if flag:
#                 return True
                
#         return False
