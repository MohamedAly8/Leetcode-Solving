# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # need to do in order
        
        stack = []
        curr = root
        
        while stack or curr:
             # there is left nodes, the smallest possible
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # if there are no more left children, stard in order            
            k -= 1
            
            curr = stack.pop()
            if k == 0:
                return curr.val
            
            
            curr = curr.right
        
        return curr.val
            

        