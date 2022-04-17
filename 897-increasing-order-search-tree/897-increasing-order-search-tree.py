# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root == None: return root
        newRoot = self.increasingBST(root.left)
        if newRoot != None:
            currRoot = newRoot
            while currRoot.right != None:
                currRoot = currRoot.right
            currRoot.right = root
            root.left = None
        else:
            newRoot = root
        root.right = self.increasingBST(root.right)
        return newRoot
  
