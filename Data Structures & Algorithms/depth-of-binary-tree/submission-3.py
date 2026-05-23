# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs 
        # base case not required, we can set ans to 0 , loop will execute and if statment wont
        # run and give ans
        if not root:
            return 0
        ans = 0
        stk = [[root,1]]
        while stk:
           node,depth = stk.pop()
           if node:
            ans = max(ans,depth)
            stk.append([node.left,depth+1])
            stk.append([node.right,depth+1])
        return ans

