'''
    https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
    104. Maximum Depth of Binary Tree
    
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Note: A leaf is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        m =[1]
        self.helper(root,1,m)
        return m[0]
    def helper(self,root,de,m):
        if not root:
            return 
        if de >m[0]:
            m[0]=de
        # print(m)
        self.helper(root.left,de+1,m)
        self.helper(root.right,de+1,m)