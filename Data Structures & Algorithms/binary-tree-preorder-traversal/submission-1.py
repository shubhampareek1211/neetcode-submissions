# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        list1 = []
        curr = root
        while curr or stk:
             if curr:
                list1.append(curr.val)
                stk.append(curr.right)
                curr = curr.left
             else:
                curr = stk.pop()
        return list1
        