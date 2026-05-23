# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case 
        # if both are null 
        if not p and not q: # both tree are empty ; checks null case
            return True
        if not p or not q: # one empty and other not ; checks one empty and other not
            return False
        
        if p.val!=q.val: # compares the value
            return False
        # recursive step
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)) # since both should be comparable

