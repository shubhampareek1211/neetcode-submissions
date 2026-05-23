# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = False
        
        def dfs(root):
            nonlocal ans
            if not root:
                return [True,0] # base case the tree will be balanced and height is 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            # from the root we checked, we also check if the left[0] and right[0] subtree is balanced
            balance = (left[0] and right[0]) and abs(left[1] - right[1])<=1 # [[bool,height]] 
            
            return [balance, 1+ max(left[1],right[1])
            ]
        return dfs(root)[0] # returning bool


        