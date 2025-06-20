# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative approach using stack.
        # if not root:
        #     return 0
        # longest = 0
        # stack = []
        # stack.append((root,1))
        # while stack:
        #     node, depth = stack.pop()
        #     if node:
        #         longest = max(longest, depth)
        #         stack.append((node.right, depth+1))
        #         stack.append((node.left, depth+1))
        # return longest
        ans = [0]
        def depthSeeker(root,depth):
            if root == None:
                return
            depth += 1
            depthSeeker(root.left,depth)
            depthSeeker(root.right,depth)
            if root.right == None and root.left == None:
                ans.append(depth)
        depthSeeker(root,0)
        return max(ans)


        
