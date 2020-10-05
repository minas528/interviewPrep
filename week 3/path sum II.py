'''
    https://leetcode.com/problems/path-sum-ii/submissions/
    113. Path Sum II
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        def do_dfs(node,s, temp, res):
            # print(node.val,s)
            # nonlocal res
            if not node.left and not node.right and s == node.val:
                temp.append(node.val)
                # print(here)
                res.append(temp)
            if node.left:
                do_dfs(node.left, s - node.val, temp+[node.val], res)
            if node.right:
                 do_dfs(node.right, s - node.val, temp+[node.val], res)
        res = []
        do_dfs(root, sum,[],res)
        return res
            