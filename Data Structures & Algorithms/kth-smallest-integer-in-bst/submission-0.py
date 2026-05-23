# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list1 = []

        def kth(node):
            if node is None:
                return
            
            list1.append(node.val)
            kth(node.left)
            kth(node.right)
        
        kth(root)

        list1.sort()
        return list1[k-1]

