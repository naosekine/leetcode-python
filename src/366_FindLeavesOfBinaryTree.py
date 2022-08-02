# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def getHeight(root):
            if root is None:
                return -1
            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)
            
            currHeight = max(leftHeight, rightHeight) + 1
            
            pairs.append((currHeight, root.val))
            
            return currHeight

        pairs = []
        getHeight(root)
        pairs.sort()
        
        currHeight = 0
        currList = []
        ans = []
        for height, val in pairs:
            if currHeight == height:
                currList.append(val)
            else:
                ans.append(currList)
                currList = []
                currList.append(val)
                currHeight = height
        if currList:
            ans.append(currList)
        return ans
                
        
# self-help solution        
#         self.memo = set()
        
#         def dfs(node, leafs):
#             if node:
#                 if (node.left is None or id(node.left) in self.memo) and (node.right is None or id(node.right) in self.memo) and id(node) not in self.memo:
#                     leafs.append(node.val)
#                     self.memo.add(id(node))
#                 dfs(node.left, leafs)
#                 dfs(node.right, leafs)
#         ans = []
#         leafs=[]
#         dfs(root, leafs)
#         while leafs:        
#             ans.append(leafs)        
#             leafs=[]
#             dfs(root, leafs)
#         return ans
            