class TreeNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.right = None
        self.left = None


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:

        newNode = TreeNode(key, val)

        if not self.root:
            self.root = newNode
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
            
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:

        curr = self.root

        while curr:
            if curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.left
            else:
                return curr.val
        return -1

    
    def findMin(self, node: TreeNode)-> TreeNode:

        while node and node.left:
            node = node.left
        
        return node
        


    def getMin(self) -> int:

        minNode = self.findMin(self.root)
        return minNode.val if minNode else -1


    def getMax(self) -> int:

        curr = self.root

        while curr and curr.right:
            curr = curr.right
        
        return curr.val if curr else -1


    def removeHelper(self, node: TreeNode, key)->None:

        if node:

            if key > node.key:
                node.right = self.removeHelper(node, key)
            elif key < node.key:
                node.left = self.removeHelper(node, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minNode = self.findMin(node.right)
                    node.val = minNode.val
                    node.key = minNode.key
                    node.right = self.removeHelper(node.right, minNode.key)
            return node
        else:
            return None


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def inorderHelper(self, node: TreeNode, result)-> None:

        if node:
            self.inorderHelper(node.left, result)
            result.append(node.key)
            self.inorderHelper(node.right, result)

    def getInorderKeys(self) -> List[int]:
        keys = []

        self.inorderHelper(self.root, keys)
        return keys