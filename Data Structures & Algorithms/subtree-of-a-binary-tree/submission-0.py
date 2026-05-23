# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subtree is empty then it's a sub part of root tree
        if not subRoot:
            return True
        # root don't exist
        if not root:
            return False
        # comparing both the tree
        if self.sameTree(root,subRoot):
            return True
        # comparing the left and right main tree to subtree, if one of then true, return true
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        

        # helper function to compare the node of root tree and subtree 
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # recursive base function 
            # none of them exist, return true
        if not root and not subRoot:
            return True
            # if one of them not exist 
        if not root or not subRoot:
            return False

            # val diff 
        if root.val!=subRoot.val:
            return False
        return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))

    
        