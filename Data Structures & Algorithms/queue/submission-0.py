class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = self.next = None

class Deque:
    def __init__(self):
        self.left = self.right = None
        
    def isEmpty(self) -> bool:
        # Should return True when empty
        return self.left is None
    
    def append(self, value: int) -> None:
        node = ListNode(value)
        if self.right:
            self.right.next = node
            node.prev = self.right
            self.right = node  # Directly assign node
        else:
            self.right = self.left = node
            
    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        if self.left:
            node.next = self.left
            self.left.prev = node
            self.left = node  # Directly assign node
        else:
            self.left = self.right = node
            
    def pop(self) -> int:
        if self.right:
            res = self.right.val
            self.right = self.right.prev
            if self.right:
                self.right.next = None  # Clean up pointer
            else:
                self.left = None  # Queue is now empty
            return res
        else:
            return -1
            
    def popleft(self) -> int:
        if self.left:
            res = self.left.val
            self.left = self.left.next
            if self.left:
                self.left.prev = None  # Clean up pointer
            else:
                self.right = None  # Queue is now empty
            return res
        else:
            return -1