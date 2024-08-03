# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [1,2,3,4,5]
        prev = None
        
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        
        return prev
