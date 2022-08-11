# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # See if tree has no left child 
            # if no left child, add to result
            
        # If there is left child, run code on left tree
        
        
        result = []
    
        def inOrder(root):

            if not root:
                return 
            
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)
        
        
        inOrder(root)
        
        return result
        
        
        
        
 
        
            
        
        
        
        