# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        carry = 0
        temp = dummy_node
        t1,t2 = l1,l2
        while l1 or l2 or carry:
            sum1 = carry
            if l1:
                sum1 += l1.val
                l1 = l1.next
            if l2:
                sum1 += l2.val
                l2 = l2.next

            NewNode = ListNode(sum1%10)
            carry = sum1//10
            temp.next = NewNode
            temp = temp.next
        


        return dummy_node.next


        