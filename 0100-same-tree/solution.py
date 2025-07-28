# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def BinaryTree(p, q):
            if p == None and q == None:
                return True
            if (p == None and q != None) or (p != None and q == None):
                return False 
            if p.val != q.val:
                return False
            return BinaryTree(p.right, q.right) and BinaryTree(p.left, q.left)
        return BinaryTree(p,q)
