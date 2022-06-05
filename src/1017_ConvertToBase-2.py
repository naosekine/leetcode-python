class Solution:
    def baseNeg2(self, n: int) -> str:
        s = ''
        if n == 0:
            return '0'
        while n != 0:
            if n % 2 != 0:
                s = '1' + s
                n = (n - 1)//-2
            else:
                s = '0' + s
                n = n//-2
        return s
        
#         rbin_n = bin(n)[2:][::-1]
#         l = list(rbin_n)
#         i = 0
#         while i < len(l):
#             if l[i] == '2':
#                 l[i] = '0'
#                 if i == len(l)-1:
#                     l.append('1')
#                 else:
#                     if l[i+1] == '0':
#                         l[i+1] = '1'
#                     elif l[i+1] == '1':
#                         l[i+1] = '2'                    
#             if i % 2 != 0 and l[i] == '1':
#                 if i == len(l)-1:
#                     l.append('1')
#                 else:
#                     if l[i+1] == '0':
#                         l[i+1] = '1'
#                     elif l[i+1] == '1':
#                         l[i+1] = '2'
#             i += 1
        
#         return ''.join(l[::-1])