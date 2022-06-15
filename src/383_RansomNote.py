from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        counter_ran = Counter(ransomNote)
        counter_mag = Counter(magazine)
                
        for cha, count in counter_ran.items():
            if count > counter_mag[cha]:
                return False
            
        return True
#         ran = {}
#         for s in ransomNote:
#             if s in ran:
#                 ran[s] += 1
#             else:
#                 ran[s] = 1
        
#         maga = {}
#         for s in magazine:
#             if s in maga:
#                 maga[s] += 1
#             else:
#                 maga[s] = 1
        
#         for key in ran.keys():
#             if key in maga:
#                 if ran[key] > maga[key]:
#                     return False
#             else:
#                 return False
#         return True