'''
    https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
    94. Binary Tree Inorder Traversal
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def tra(node,arr):
            if not node:
                return None
            tra(node.left,arr)
            arr.append(node.val)
            tra(node.right,arr)
        res =[]
        tra(root,res)
        return res