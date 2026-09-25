# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current != None:
            #save where were going next
            next2 = current.next
            #point curr node to prev
            current.next = prev
            #prev moves forward
            prev = current
            #current moves forward to our saved node (next2)
            current = next2
        return(prev)
        
