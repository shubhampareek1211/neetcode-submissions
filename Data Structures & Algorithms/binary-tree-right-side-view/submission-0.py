# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        ans = []

        while q:
            rightside = 0 # rightmost element
            for i in range(len(q)): # each level travesal
                node = q.popleft()
                if node: # if not null, update right side
                    rightside = node # rightmost node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                ans.append(rightside.val)
        return ans

