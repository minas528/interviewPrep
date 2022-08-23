# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        reveresed = None
        slow = head
        fast = head
        while fast and fast.next:
            temp = slow
            
            slow = slow.next
            fast = fast.next.next
            
            temp.next = reveresed
            reveresed = temp
        if fast:
            slow = slow.next
            
        
        while reveresed and reveresed.val == slow.val:
            reveresed = reveresed.next
            slow = slow.next
        return reveresed == None