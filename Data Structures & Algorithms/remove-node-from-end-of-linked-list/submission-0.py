# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        forward = head
        dummy = ListNode(0,head)
        left = dummy

        while n>0:
            forward = forward.next
            n -= 1

        while forward:
            left = left.next
            forward = forward.next

        left.next = left.next.next
        return dummy.next

          