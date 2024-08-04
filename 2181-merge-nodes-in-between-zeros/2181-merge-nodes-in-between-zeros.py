# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        res = node
        sumOf = 0

        while head:
            if head.val == 0:
                res.next = ListNode(sumOf)
                res = res.next
                print(res.next)
                sumOf = 0
            else:
                sumOf += head.val
            head = head.next
        
        node = node.next
        return node.next