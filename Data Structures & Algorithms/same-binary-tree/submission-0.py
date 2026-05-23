# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list1 = []

        def leftTree(node):
            if not node:
                list1.append(None)
                return
            list1.append(node.val)
            leftTree(node.left)
            leftTree(node.right)
        leftTree(p)

        list2 = []

        def rightTree(node):
            if not node:
                list2.append(None)
                return 
            list2.append(node.val)
            rightTree(node.left)
            rightTree(node.right)
        rightTree(q)

        return list1==list2
                
        