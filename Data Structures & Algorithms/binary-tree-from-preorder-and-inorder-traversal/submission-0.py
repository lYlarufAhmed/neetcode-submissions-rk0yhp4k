# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Some improvements:
        # 1. have pointer to read the root instead of passing the whole array in each call
        # 2. create a hashmap to get the root index.
        # To achieve both of this we need a helper function

        self.root_index = 0
        self.inorder_index_map = {value: key for key, value in enumerate(inorder)}


        def helper(left_index, right_index):
            #base case
            if left_index > right_index:
                return None
            root_val = preorder[self.root_index]
            self.root_index += 1

            root = TreeNode(root_val)

            inorder_root_index = self.inorder_index_map.get(root_val)

            root.left = helper(left_index, inorder_root_index-1)
            root.right = helper(inorder_root_index+1,right_index)
            
            return root


        
        return helper(0, len(inorder)-1)