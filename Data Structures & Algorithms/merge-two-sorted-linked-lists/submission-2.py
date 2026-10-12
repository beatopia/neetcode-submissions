# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #make third list, append smaller until both next are None
        dummy = ListNode()
        head = dummy
        while list1 or list2:
            if list1 is None and list2:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            elif list2 is None and list1:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
            elif list1.val >= list2.val:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            elif list2.val >= list1.val:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
        return(head.next)
        