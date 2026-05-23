# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case 
        if not head:
            return None

        prev = None
        curr = head 

        while curr:
            temp_pt = curr.next  
            curr.next = prev # reversing the pointer of current;  initally to null
            prev = curr
            curr = temp_pt
        
        # previous is now head, after loop ends 

        return prev
        