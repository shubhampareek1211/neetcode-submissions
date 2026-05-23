# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode()
        temp = dummy_head

        while list1!=None and list2!=None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next 
            temp = temp.next 
        # if one of the list is null just insert at the other list to the temp
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy_head.next
        

        