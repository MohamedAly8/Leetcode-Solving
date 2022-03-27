# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        orig = head
        while(head):
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return orig
            
        