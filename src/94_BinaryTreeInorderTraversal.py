# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        inorder_list = []
        if root:
            self.inorderTraversal(root.left)
            inorder_list.append(root.val)
            self.inorderTraversal(root.right)
            return inorder_list
    
if __name__ == '__main__':
    # root1 = [1,null,2,3]    
    root1 = cur1 = TreeNode(1)
    cur1.right = TreeNode(2)
    cur1 = cur1.right
    cur1.left = TreeNode(3)
    
    # root2 = []
    root2 = None
    
    # root3 = [1]
    root3 = TreeNode(1)

    s = Solution()
    print(s.inorderTraversal(root1))
    print(s.inorderTraversal(root2))
    print(s.inorderTraversal(root3)) 