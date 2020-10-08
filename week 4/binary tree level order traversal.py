'''
    https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/
    107. Binary Tree Level Order Traversal II

    Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        def tra(root,level,res):
            if not root:
                return
            # print(root.val)
            if len(res)>level:
                res[level].append(root.val)
            else:
                res.append([root.val])
            tra(root.left,level+1,res)
            tra(root.right,level+1,res)
        res=[]
        tra(root,0,res)
        return res[::-1] 
