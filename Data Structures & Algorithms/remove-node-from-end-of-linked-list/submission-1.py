# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy_node =ListNode(-1)
        dummy_node.next = head
        pt1 = dummy_node
        pt2 = head
        
        while n>0:
            pt2 = pt2.next
            n -=1

        while pt2:
            pt1 = pt1.next
            pt2 = pt2.next

        pt1.next = pt1.next.next

        return dummy_node.next

        