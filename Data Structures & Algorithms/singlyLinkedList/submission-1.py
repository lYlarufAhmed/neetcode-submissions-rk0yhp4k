class LinkedNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        i = 0
        curr = self.head
        while i != index:
            curr = curr.next
            i += 1
        return curr.value

        

    def insertHead(self, val: int) -> None:
        node = LinkedNode(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.head = LinkedNode(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = LinkedNode(val)
        self.size += 1

        

    def remove(self, index: int) -> bool:
        if -1 < index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                i = 0
                curr = self.head
                prev = None
                while i != index:
                    prev, curr = curr, curr.next
                    i += 1
                prev.next = curr.next
            self.size -= 1
            return True
        return False
        

    def getValues(self) -> List[int]:
        res = []

        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
        
