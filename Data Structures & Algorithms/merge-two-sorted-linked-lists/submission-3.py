# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create dummy node
        #if either l1 or l2 is None, dummy.next is the one that exists
        #otherwise, dummy.next is the smaller of l1 and l2
        #return head.next because our dummy node is initialized with 0 as first val

        dummy = ListNode()
        curr = dummy
        while list1 or list2:
            if not list1 and list2:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            elif not list2 and list1:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            elif list2.val >= list1.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            elif list1.val >= list2.val:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        return(dummy.next)
