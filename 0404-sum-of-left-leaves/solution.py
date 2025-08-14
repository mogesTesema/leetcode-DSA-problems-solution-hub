# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        def inorder(node,isLeft=False):
            if node == None:
                return
            left = inorder(node.left,True)
            right = inorder(node.right)
            if isLeft and left == None and right==None:
                nonlocal total
                total += node.val
        inorder(root)
        return total# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # We need a separate variable to accumulate the sum.
        # A list or an array of size 1 can be used to simulate
        # a mutable integer, or we can use a helper function that returns the sum.
        # This approach avoids the nonlocal keyword, which can be cleaner.

        def dfs(node):
            if not node:
                return 0
            
            current_sum = 0
            
            # Check if the left child exists and is a leaf node.
            # A leaf node has no children.
            if node.left and not node.left.left and not node.left.right:
                current_sum += node.left.val
            
            # Recursively calculate the sum for the left and right subtrees.
            current_sum += dfs(node.left)
            current_sum += dfs(node.right)
            
            return current_sum
        
        return dfs(root)

        
