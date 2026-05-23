# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head 
        count = 1
        while temp and temp.next:
            temp = temp.next
            count +=1
        
        index = count - n
        if index==0:
            return head.next

        temp = head 
        for i in range(count-1):
            if (i+1) == index:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head 

