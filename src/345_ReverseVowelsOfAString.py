class Solution:
    def reverseVowels(self, s: str) -> str:        
        vowels = {'a', 'i', 'u', 'e', 'o', 'A','I','U','E','O'}
        list_s = list(s)
        front = 0
        back = len(s) -1
        
        while front < back:
            if list_s[front] in vowels and list_s[back] in vowels:
                temp = list_s[front]
                list_s[front] = list_s[back]
                list_s[back] = temp
                front += 1
                back -= 1
            elif list_s[front] in vowels:
                back -= 1
            elif list_s[back] in vowels:
                front += 1
            else:
                front += 1
                back -= 1
        return ''.join(list_s)
     
#         b_set = {'a', 'i', 'u', 'e', 'o', 'A','I','U','E','O'}
#         b_k_idxs = []
#         stack_b=[]
#         queue_k=[]
        
#         for ele in s:
#             if ele in b_set:
#                 b_k_idxs.append('b')
#                 stack_b.append(ele)
#             else:
#                 b_k_idxs.append('k')
#                 queue_k.append(ele)
                
#         r_s = ''
#         queue_i = 0
#         for b_or_k in b_k_idxs:
#             if b_or_k == 'b':
#                 r_s += stack_b.pop()
#             else:
#                 r_s += queue_k[queue_i]
#                 queue_i += 1
#         return r_s
                
        
        