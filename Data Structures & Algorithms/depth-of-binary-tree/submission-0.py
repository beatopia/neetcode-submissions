# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #depth = 1+max(hr, hl)
        node = root
        def height(node):
            if node is None:
                return(0)
            
            
            lh = height(node.left)
            rh = height(node.right)
            h = max(lh,rh)
            return(1+max(lh, rh))
        
        return(height(node))

            

            
