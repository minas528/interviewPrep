'''
    https://leetcode.com/contest/weekly-contest-209/problems/even-odd-tree/
    1609. Even Odd Tree
    Dificulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        lev = {}
        self.tra(root, 0, lev)
        print(lev)
        for i,arr in lev.items():
            if i%2 ==0:
                if arr[0]%2==0:
                    return False
                for j in range(1,len(arr)):
                    if arr[j]%2==0:
                        return False
                    if arr[j-1]>=arr[j]:
                        return False
            else:
                if arr[0]%2==1:
                    return False
                for j in range(1,len(arr)):
                    if arr[j]%2==1:
                        return False
                    if arr[j-1]<=arr[j]:
                        return False
        return True
                    
    def tra(self, root,level, arr):
        if not root:
            return
        if level in arr:
            arr[level].append(root.val)
        else:
            arr[level]= [root.val]
        self.tra(root.left, level+1, arr)
        self.tra(root.right, level+1, arr)
