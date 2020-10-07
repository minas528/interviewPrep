'''
    https://leetcode.com/problems/find-largest-value-in-each-tree-row/submissions/
    515. Find Largest Value in Each Tree Row
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        largest_vals = []
        self.helper(root, largest_vals, 0)
        return largest_vals
        
    def helper(self,root, largest_vals, level):
        if not root:
            return
        if level == len(largest_vals):
            largest_vals.append(root.val)
        else:
            largest_vals[level] = max(largest_vals[level], root.val)
        self.helper(root.left,largest_vals, level+1)
        self.helper(root.right,largest_vals, level +1)