"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # creating a copy of the original list without random pointer and next pointer
        temp1 = head
        hashmap = {None:None} # if hashmap is null it should return null
        # creating a hash table to store the index
        while temp1:
            copy = Node(temp1.val)
            hashmap[temp1] = copy
            temp1 = temp1.next
        
        temp1 = head
        while temp1:
            # get the copy node and set pointer 
            copy = hashmap[temp1] # copy is hashmap temp1 
            copy.next = hashmap[temp1.next]
            copy.random = hashmap[temp1.random]
            temp1 = temp1.next
        return hashmap[head]




        # adding the random pointers and next pointer with the copy node with the help of hashmap





        

        

