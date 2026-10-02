# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #swap left with right
        node = root
        def swap(node):
            if node is None:
                return
            cur_left = node.left
            cur_right = node.right

            node.left = cur_right
            node.right = cur_left
            swap(node.left)
            swap(node.right)
        swap(node)
        return(node)