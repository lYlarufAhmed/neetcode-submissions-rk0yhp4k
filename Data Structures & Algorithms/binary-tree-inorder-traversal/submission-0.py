# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderHelper(self, root, num=[]):
        if not root:
            return num
        # num.append(root.val)
        
        self.inorderHelper(root.left, num)
        num.append(root.val)
        self.inorderHelper(root.right, num)

        return num
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderHelper(root, [])