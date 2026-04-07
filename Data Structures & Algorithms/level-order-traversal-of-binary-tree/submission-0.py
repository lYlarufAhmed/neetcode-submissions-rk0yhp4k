# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []
        if root:
            queue.append([root])
        
        res = []

        while len(queue):
            curr = queue.pop(0)
            arr = []
            q = []
            for node in curr:
                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(q):
                queue.append(q)
            res.append(arr)
        return res


        