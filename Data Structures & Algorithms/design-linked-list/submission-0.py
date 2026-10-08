class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1) # dummy head
        self.tail = ListNode(-1) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index: int) -> ListNode:
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.getPrev(index).next.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode
        self.size += 1


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        prev = self.getPrev(index)   # node before insertion point
        nxt  = prev.next
        node = ListNode(val)
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node
        self.size += 1        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.getPrev(index)
        cur  = prev.next
        nxt  = cur.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)