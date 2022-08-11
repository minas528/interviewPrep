# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node,left,right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            
            return dfs(node.left,left,node.val) and dfs(node.right,node.val,right)
        
        import sys
        right = sys.maxsize
        left = -sys.maxsize -1
        return dfs(root,left,right)