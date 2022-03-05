# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isBST(root, float('inf'), float('-inf'))
    
    def isBST(self, node, maxi, mini):

        if node is None:
            return True

        if (node.val <= mini or node.val >= maxi):
            return False
        l = self.isBST(node.left, node.val, mini)
        r = self.isBST(node.right, maxi, node.val)
        return l and r