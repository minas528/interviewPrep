# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        q_original = deque([original])
        q_cloned = deque([cloned])

        while q_original:
            node_orginal = q_original.popleft()
            node_cloned = q_cloned.popleft()
            if node_orginal == target:
                return node_cloned
            if node_orginal.left:
                q_cloned.append(node_cloned.left)
                q_original.append(node_orginal.left)
            if node_orginal.right:
                q_cloned.append(node_cloned.right)
                q_original.append(node_orginal.right)

