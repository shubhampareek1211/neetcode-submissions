# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stk1 = []
        stk2 = []
        stk1.append(root)
        while stk1:
           curr =  stk1.pop()
           stk2.append(curr)
           if curr.left:
            stk1.append(curr.left)
           if curr.right:
            stk1.append(curr.right)
        
        result = []
        while stk2:
            result.append(stk2.pop().val)

        return result
        