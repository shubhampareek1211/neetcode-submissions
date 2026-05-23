# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,int_max):
            if not node:
                return 0
            result = 0


            if node.val >= int_max:
                int_max = max(int_max,node.val)
                result +=1
            # add results from the left and right subtree 

            result += dfs(node.left,int_max)
            result += dfs(node.right,int_max)
            return result
        return dfs(root,root.val)
