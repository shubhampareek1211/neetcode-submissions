# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def height(root):
            # decaring a non local varaible 
            nonlocal result 
            
            if not root:
                return 0
            leftH =  height(root.left)
            rightH = height(root.right)
            diameter = leftH + rightH
            result = max(result,diameter) # maintaing the max diameter at any point
           # height returned to the parent 

            return 1 + max(leftH,rightH)

        height(root)

        return result


        