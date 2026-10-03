# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return(False)
        skip1 = head.next
        skip2 = skip1.next
        
        if skip2 is None or skip1 is None:
            return(False)
        
        while skip2 and skip2.next:
            skip2 = skip2.next.next
            skip1 = skip1.next
            if skip2 == skip1:
                return(True)
        return(False)

