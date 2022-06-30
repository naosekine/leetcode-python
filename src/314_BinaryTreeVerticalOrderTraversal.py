# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root = root, rightlvl = 0, depthlvl = 0):
            if root is not None:
                node_lvl_map.append((rightlvl, depthlvl, root.val))
                dfs(root.left, rightlvl -1, depthlvl + 1)
                dfs(root.right, rightlvl + 1, depthlvl + 1)
                
        node_lvl_map = []       
        dfs()
        node_lvl_map.sort(key=lambda x : (x[0], x[1]))
        
        ans = []
        last_rightlvl = None
        for rightlvl, depthlvl, val in node_lvl_map:
            if last_rightlvl == rightlvl:
                ans[-1].append(val)
            else:
                ans.append([val])
            last_rightlvl = rightlvl
            
        return ans
                
