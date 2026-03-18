# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = 0

        def travers(node,x):
            nonlocal max_depth
            if not node:
                max_depth = max(max_depth,x)
                return
                
            travers(node.left,x+1)
            travers(node.right,x+1)

        travers(root,0)

        return max_depth
        
