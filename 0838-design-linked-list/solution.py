class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        counter = 0
        currentPointer = self.head
        while currentPointer:
            if counter == index:
                return currentPointer.val
            currentPointer = currentPointer.next
            counter += 1
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head ==None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        currentPointer = self.head
        while currentPointer.next:
            currentPointer = currentPointer.next
        currentPointer.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        currentPointer = self.head
        counter = 0
        while currentPointer:
            if counter == index - 1:
                new_node = Node(val)
                new_node.next = currentPointer.next
                currentPointer.next = new_node
                return
            currentPointer = currentPointer.next
            counter += 1
       

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return
        currentPointer = self.head
        counter = 0
        while currentPointer.next:
            if counter == index - 1:
                currentPointer.next = currentPointer.next.next
                return
            currentPointer = currentPointer.next
            counter += 1
        # If index is out of bounds, do nothing (based on problem description)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
