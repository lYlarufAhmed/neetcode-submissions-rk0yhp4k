# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        def helper(root, depth=0, answer=0):
            if not root:
                return depth
            

            if not root.left and not root.right:
                return max(depth+1, answer)
            
            if root.left:
                answer = max(helper(root.left, depth+1, answer), answer)
            
            if root.right:
                answer = max(helper(root.right, depth+1, answer), answer)
            

            return answer

        return helper(root)
        