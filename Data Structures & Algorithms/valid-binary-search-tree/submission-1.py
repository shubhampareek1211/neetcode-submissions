# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        
        def validnode(node,left,right):
            if not node:
                return True
            
            if not (left < node.val and right>node.val):
                return False
            
            return validnode(node.left,left,node.val)  and validnode(node.right,node.val,right)
        return validnode(root,float("-inf"),float("inf"))

            




        