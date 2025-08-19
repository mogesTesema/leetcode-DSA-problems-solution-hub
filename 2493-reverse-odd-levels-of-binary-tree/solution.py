# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node_one, node_two, is_odd_level):
            if not node_one: return
            if is_odd_level:
                node_one.val, node_two.val = node_two.val, node_one.val
            dfs(node_one.left, node_two.right, not is_odd_level)
            dfs(node_one.right, node_two.left, not is_odd_level)
        dfs(root.left,root.right, True)
        return root
        
