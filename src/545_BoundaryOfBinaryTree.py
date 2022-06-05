# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, t):
        return t.left == None and t.right == None

    def addLeaves(self, res, root):
        if self.isLeaf(root):
            res.append(root.val)
        else:
            if root.left:
                self.addLeaves(res, root.left)
            if root.right:
                self.addLeaves(res, root.right)    

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        # print(self.isLeaf(root))
        if not self.isLeaf(root):
            res.append(root.val)
        
        t = root.left
        while t:
            if not self.isLeaf(t):
                res.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        
        self.addLeaves(res, root)
        s = []
        t = root.right
        while t:
            if not self.isLeaf(t):
                s.append(t.val)
            
            if t.right:
                t= t.right
            else:
                t = t.left
        
        while s:
            res.append(s.pop())
        
        return res