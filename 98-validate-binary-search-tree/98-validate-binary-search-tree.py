# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        return self.isBST(root, INT_MAX, INT_MIN)
    
    
    def isBST(self, node, maxi, mini):

        if node is None:
            return True

        if (node.val < mini or node.val > maxi):
            return False

        return self.isBST(node.left, node.val-1, mini) and self.isBST(node.right, maxi, node.val+1)