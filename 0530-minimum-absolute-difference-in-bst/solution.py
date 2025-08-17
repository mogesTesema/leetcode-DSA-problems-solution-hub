# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_one = roo.val
        min_two = 0
        def leftDepth(node):
            if node == None:
                return# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node, prev, diff_min):

            if not node:
                return prev, diff_min

            prev, diff_min = inorder(node.left, prev, diff_min)

            if prev is not None:
                diff_min = min(abs(node.val - prev ), diff_min)
            prev = node.val
            return inorder(node.right, prev, diff_min)
        

        _, ans = inorder(root, None, float('inf'))
        return ans
            
        
