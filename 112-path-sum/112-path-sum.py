# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        q = deque()
        
        if not root:
            return False
        
        q.append((root,0))
        
        while q:
            node, currSum = q.popleft()
            
            if not node.left and not node.right:
                if currSum + node.val == targetSum:
                    return True

                
            if node.left:
                q.append((node.left, node.val + currSum))
            if node.right:
                q.append((node.right, node.val + currSum))
        
        
        return False