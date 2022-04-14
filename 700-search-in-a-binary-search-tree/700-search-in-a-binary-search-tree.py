# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == val:
                return cur
            elif cur.val > val and cur.left:
                stack.append(cur.left)
            elif cur.right:
                stack.append(cur.right)
            else:
                return None