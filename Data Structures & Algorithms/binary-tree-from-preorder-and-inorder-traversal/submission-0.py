# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case for the recursive function 
        if not preorder or not inorder:
            return None 
        
        root = TreeNode(preorder[0])
        # finding index of root value in inorder and calling it mid
        mid = inorder.index(preorder[0])
        # building left subtree from after 1st and till mid of preorder
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        