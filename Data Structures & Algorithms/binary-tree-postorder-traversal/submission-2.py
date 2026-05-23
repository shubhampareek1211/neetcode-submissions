# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = [root]
        visit = [False]
        res = []
        while stk:
            curr = stk.pop() # this will take care the else case 
            v =  visit.pop() # that is pop when curr pointer is null and we need to pop anyway
            if curr:
                if v:
                    res.append(curr.val) # if visited then easily add to res
                else:  # go to left and right and add them into stack
                    stk.append(curr)
                    visit.append(True)
                    stk.append(curr.right)
                    visit.append(False)
                    stk.append(curr.left)
                    visit.append(False)
        return res


        