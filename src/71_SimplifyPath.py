class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split('/')
        for path in path_list:
            # print(path)
            # print(stack)
            if path == '.':
                continue
            elif path == '..':
                if len(stack) > 0:
                    stack.pop()
            elif path == '':
                continue
            else:
                stack.append(path)
        
        if stack:
            return ''.join([ '/' + path for path in stack])
        else:
            return '/'
        
#         path_list = path.split('/')
#         path_list = [s for s in path_list if s != '']
#         print(path_list)
        
#         del_path = set()
#         for i, path in enumerate(path_list):
#             if path == '.':
#                 del_path.add(i)
#             if path == '..':
#                 del_path.add(i)
#                 while i-1 in del_path:
#                     i -= 1
#                 del_path.add(i-1)
                
#         print(del_path)
#         ans = ""
#         for i, path in enumerate(path_list):
#             if i not in del_path:
#                 ans += "/" + path
#         if ans:
#             return ans
#         else:
#             return '/'