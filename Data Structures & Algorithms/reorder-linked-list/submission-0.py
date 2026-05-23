# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding the middle 
        slow = head 
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # splitting the second and first half 
        mid = slow.next
        slow.next = None
        prev = None
        # reversing the second half ; three pointer prev, mid and temp
        while mid:
            temp = mid.next
            mid.next = prev 
            prev = mid
            mid = temp
        


        l1 = head # pointer at 1st half begging 
        l2 = prev # pointer at the end of second half 

        while l2: # since second can be shorter then first after split
            # taking temp to exchange 

            temp1 = l1.next # storing the pointer of next with temp
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1
            l1 = temp1 # shifting the pointer 
            l2 = temp2



        