# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # solution with iterative approach
        # if not root:
        #     return False
        # plus = root.val
        # bfs = deque([(root,plus)])
        # while bfs:
        #     node,curr_sum = bfs.popleft()
        #     if (not node.left and not node.right) and curr_sum == targetSum:
        #         return True
        #     if node.left and node.right:
        #         curr_sum+=node.left.val
        #         bfs.append((node.left,curr_sum))
        #         curr_sum = curr_sum - node.left.val + node.right.val
        #         bfs.append((node.right,curr_sum))
        #     elif node.left:
        #         curr_sum+=node.left.val
        #         bfs.append((node.left,curr_sum))
        #     elif node.right:
        #         curr_sum+=node.right.val
        #         bfs.append((node.right,curr_sum))
        #solution with recursive approach.
        found = False
        def routing(root,previousSum):
            if root == None:
                return 
            previousSum += root.val
            routing(root.left,previousSum)
            routing(root.right,previousSum)
            if root.right == None and root.left == None:
                if previousSum == targetSum:
                    nonlocal found
                    found = True
                    return
        routing(root,0)
        
        return (found)
        
