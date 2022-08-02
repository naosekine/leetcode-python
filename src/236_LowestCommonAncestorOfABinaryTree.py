# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.inorder_list = []
        self.preorder_list = []
        def inorder(node):
            if node:
                inorder(node.left)
                self.inorder_list.append(node)
                inorder(node.right)
            return self.inorder_list
            
        def preorder(node):
            if node:
                self.preorder_list.append(node)
                preorder(node.left)
                preorder(node.right)
                return self.preorder_list
        
        inorder_list = inorder(root)
        preorder_list = preorder(root)
        
        p_idx = inorder_list.index(p)
        q_idx = inorder_list.index(q)
        
        for parent in preorder_list:
            if inorder_list[p_idx] == parent or inorder_list[q_idx] == parent:
                return parent
            parent_idx = inorder_list.index(parent)
            if (p_idx < parent_idx and q_idx > parent_idx) or (p_idx > parent_idx and q_idx < parent_idx):
                return parent
            