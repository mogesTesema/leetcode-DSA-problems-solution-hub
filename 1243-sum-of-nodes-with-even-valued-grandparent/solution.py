# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.evenValue = 0
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def evenFinder(root):
            if root == None:
                return
            if root.val % 2 == 0:
                checker(root)
            evenFinder(root.left)
            evenFinder(root.right)
        def checker(root):
            if root.left:
                if root.left.left: self.evenValue += root.left.left.val
                if root.left.right: self.evenValue += root.left.right.val
            if root.right:
                if root.right.left: self.evenValue += root.right.left.val
                if root.right.right: self.evenValue += root.right.right.val
        evenFinder(root)
        return self.evenValue
        
