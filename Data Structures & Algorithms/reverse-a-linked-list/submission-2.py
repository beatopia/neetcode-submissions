# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #for each node, 
        prev = None
        current = head
        while current:
            #save curr.next so we can jump to it
            #point current to prev
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return(prev)
            