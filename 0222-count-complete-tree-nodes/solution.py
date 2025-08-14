# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        total_node = 0
        def preOrder(node):
            if node == None:
                return 
            nonlocal total_node
            total_node +=1
            if node.left:
                preOrder(node.left)
            if node.right:
                preOrder(node.right)
        preOrder(root)
        return total_node
