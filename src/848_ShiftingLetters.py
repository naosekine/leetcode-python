class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        X = sum(shifts) % 26
        for i, word in enumerate(s):
            index = ord(word) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26
        
        return ''.join(ans)

# 
#         alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#         alp_dic = {}
#         for i,al in enumerate(alp):
#             alp_dic[al] = i
            
#         list_S = list(s)
#         shift = sum(shifts) % 26
#         for i in range(len(list_S)):
#             if alp_dic[list_S[i]]+shift < len(alp):
#                 list_S[i] = alp[alp_dic[list_S[i]]+shift]
#             else:
#                 n = (alp_dic[list_S[i]]+shift) // len(alp)
#                 list_S[i] = alp[alp_dic[list_S[i]]+shift-(len(alp))*n]
#             shift = (shift - shifts[i]) % len(alp)
#         return ''.join(list_S)