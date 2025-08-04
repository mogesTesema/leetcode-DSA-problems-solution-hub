# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
what is in order: left node right 3,2,4,1 and 4,2,3,1
        post order: left right node
        pre order: node left right
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # left = []
        # right = []
        # def inorder(node,arr):
        #     if node == None:
        #         arr.append("null")
        #         return 
        #     inorder(node.left,arr)
        #     arr.append(node.val)
        #     inorder(node.right,arr)
        # if root != None:
        #     inorder(root.left,left)
        #     inorder(root.right,right)
        # return left == right[::-1]
        def is_mirror(node_one,node_two):
            if not node_one and not node_two:
                return True
            if not node_one or not node_two:
                return False
            return (node_one.val == node_two.val and is_mirror(node_one.left,node_two.right) and is_mirror(node_one.right, node_two.left))
        
        return is_mirror(root.left, root.right)

        
