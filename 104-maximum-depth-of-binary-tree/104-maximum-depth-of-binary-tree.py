# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Depth of left vs right tree
        
        
        # Base case: empty tree
        
        
        def DFS(root):
            
            if not root:
                return 0;

            if not root.left and not root.right:
                return 1

            return max(DFS(root.left)+1, DFS(root.right)+1)
        
        return DFS(root)
        
            