# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if node:
                inorder(node.left)
                output.append(node)
                inorder(node.right)
                
        output = []
        inorder(root)
        ans = cur = TreeNode(None)
        for node in output:
            node.left = None
            cur.right = node
            cur = cur.right
        
        return ans.right
