# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        last = head
        while(last and last.next):
            curr = curr.next
            last = last.next.next          
        
        stack = []
        count = 0
        
        while(curr):
            stack.append(curr.val)
            curr = curr.next
            count += 1
        
        while(head and count != 0):
            if head.val != stack.pop():
                return False
            count -= 1
            head = head.next
            
        return len(stack) == 0