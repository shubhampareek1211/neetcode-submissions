# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # calculating height as max of height at left and right subtree at any moment of tree
        if not root:
            return 0

        lefthieght = self.maxHeight(root.left)
        righthieght = self.maxHeight(root.right)
        diameter = lefthieght + righthieght

        ans = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(diameter,ans)
        
        # height of the tree 
    def maxHeight(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftH = self.maxHeight(root.left)
        rightH = self.maxHeight(root.right)

        return 1 + max(leftH,rightH)
        


 
