# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currentKey = 0
        def dfs(root):
            nonlocal currentKey
            if not root:
                return
            dfs(root.right)
            currentKey += root.val
            root.val = currentKey
            dfs(root.left)
        dfs(root)
        return root
        
