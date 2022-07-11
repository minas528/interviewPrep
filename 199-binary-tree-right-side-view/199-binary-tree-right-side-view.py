# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        Q = collections.deque()
        Q.append(root)
        while Q:
            n = len(Q)
            curr = []
            for i in range(n):
                node = Q.popleft()
                curr.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            # print(curr)
            res.append(curr[-1])
        return res
        