class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2: return list(words[0])
        
        first_characters = set(words[0])
        ans = []
        for cha in first_characters:
            n = min([word.count(cha) for word in words])
            # print(n, cha)
            if n > 0:
                for _ in range(n):
                    ans.append(cha)
        return ans
        
        
# self-help solution
# from collections import Counter
#         l = []
#         for word in words:
#             c_w = Counter(word)
#             l.append(c_w)
            
#         print(l)
#         alp_set = set()
#         for c in l:
#             for i in c.keys():
#                 alp_set.add(i)
        
#         dic = {}
        
#         for alp in alp_set:
#             for c in l:
#                 if alp in dic:
#                     dic[alp] = min(c[alp], dic[alp])
#                 else:
#                     dic[alp] = c[alp]
#         ans = []
#         for i in dic.keys():
#             if dic[i] != 0:
#                 for j in range(dic[i]):
#                     ans.append(i)
#         return ans