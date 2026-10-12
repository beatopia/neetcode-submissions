# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split list in half, round down
        #find len of list, ceil div 2
        node = head
        length = 0
        while node:
            node = node.next
            length+=1
        half_length = -(-(length)//2)
        
        #go to half_length, save head of both lists
        #set node.next to None at half_length
        node = head
        for i in range(half_length-1):
            node = node.next
        list2 = node.next
        node.next = None
        list1 = head

        #reverse 2nd half
        prev = None
        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt
        #prev is new head

        list2 = prev
        #combine lists
        dummy = ListNode()
        res = dummy
        while list1 or list2:
            if list1 and list2:
                dummy.next = list1
                dummy = dummy.next
                list1=list1.next
                dummy.next = list2
                list2=list2.next
                dummy=dummy.next
            elif list1 and not list2:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
            elif list2 and not list1:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
                

        #return head of new list
