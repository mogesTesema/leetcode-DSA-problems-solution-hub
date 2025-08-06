# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the depth is 0
        if not root:
            return 0

        # If a node is a leaf (has no children), the depth is 1
        if not root.left and not root.right:
            return 1

        # If a node has only a left child, the min depth is 1 + the min depth of the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1

        # If a node has only a right child, the min depth is 1 + the min depth of the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1

        # If a node has both children, the min depth is 1 + the minimum of the min depths of the two subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
