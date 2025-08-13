# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        level_order = []
        q = deque([root])
        while q:
            current_list = []
            level_size = len(q)
            # iterate through the same level nodes
            for _ in range(level_size):
                node = q.popleft()
                current_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_order.append(current_list)
        return level_order
        
