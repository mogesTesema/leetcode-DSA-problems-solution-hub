# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node):
            # Base case: an empty node has a height of 0 and is balanced
            if not node:
                return 0

            # Recursively get the height and balance status of left and right subtrees
            left_height = check_balance_and_height(node.left)
            right_height = check_balance_and_height(node.right)

            # If either subtree is unbalanced (indicated by -1), propagate -1
            if left_height == -1 or right_height == -1:
                return -1

            # Check if the current node's subtrees are balanced
            if abs(left_height - right_height) > 1:
                return -1  # Unbalanced at this node

            # If balanced, return the height of the current subtree
            return 1 + max(left_height, right_height)

        # The tree is balanced if the initial call does not return -1
        return check_balance_and_height(root) != -1
