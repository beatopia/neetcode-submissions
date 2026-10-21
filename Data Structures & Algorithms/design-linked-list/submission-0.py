class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()


    def get(self, index: int) -> int:
        get = self.head.next
        for _ in range(index):
            if get and get.next:
                get = get.next
            else:
                return(-1)
        if get:
            return(get.val)
        else:
            return(-1)

    def addAtHead(self, val: int) -> None:
        new_first = ListNode(val)
        old_first = self.head.next
        self.head.next = new_first
        new_first.next = old_first

    def addAtTail(self, val: int) -> None:
        tail = ListNode(val)
        node = self.head
        while node.next:
            node = node.next
        node.next = tail

    def addAtIndex(self, index: int, val: int) -> None:
        
        #case: index = len of list or invalid
        find_len = self.head.next
        length = 0
        while find_len:
            length+=1
            find_len=find_len.next
        if length == index:
            self.addAtTail(val)
            return
        elif index > length:
            return
        #case: index is valid
        new_node = ListNode(val)
        node = self.head
        for _ in range(index):
            node = node.next
        nxt = node.next
        node.next = new_node
        new_node.next = nxt
            

    def deleteAtIndex(self, index: int) -> None:
        #case: index not valid
        find_len = self.head.next
        length = 0
        while find_len:
            length+=1
            find_len=find_len.next
        if index >= length:
            return
        #case: index valid
        node = self.head
        for _ in range(index):
            node = node.next
        node.next = node.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)