# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = [True]
        def dfs(root):
            if root:
                leftCount = dfs(root.left)
                rightCount = dfs(root.right)
                if abs(leftCount-rightCount)>1:
                    isBalanced[0] = False
                return max(leftCount, rightCount)+1
            return 0
        
        dfs(root)
        return isBalanced[0]