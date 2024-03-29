# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def dfs(node, curSum):

            if not node:
                return
    
            curSum += node.val

            if curSum == targetSum and node.left is None and node.right is None:
                return True
            
            return dfs(node.left, curSum) or dfs(node.right, curSum)
   
        return dfs(root,0)
