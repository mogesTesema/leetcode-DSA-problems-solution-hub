# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = {0: 1}  # prefix sum 0 occurs once (empty path)
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            # Number of valid paths ending here
            count = prefix_count.get(curr_sum - targetSum, 0)
            
            # Add current sum to prefix map
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
            
            # Explore children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # Backtrack (remove current sum count)
            prefix_count[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)

        
