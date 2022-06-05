"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        def dfs(root):
            if not root:
                return
            
            l.append(root.val)
            if root.children:
                lenc = len(root.children)
                for i in range(lenc):
                    dfs(root.children[i])
        
        dfs(root)
        return l
            