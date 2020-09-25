'''
    https://leetcode.com/problems/binary-search-tree-iterator/solution/
    173. Binary Search Tree Iterator
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.traverse(root, self.stack)
        self.curr = 0
        self.has_next = True 
        
        
    def _traverse(self, root, stack):
        if not root:
            return
        self.traverse(root.left,stack)
        stack.append(root.val)
        self.traverse(root.right, stack)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.stack[self.curr]
        self.curr += 1
        if len(self.stack) == self.curr:
            self.has_next = False
        return res
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.has_next if self.stack else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()