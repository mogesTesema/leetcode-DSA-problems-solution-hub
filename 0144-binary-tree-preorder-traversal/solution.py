# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # rights =[]
        # head = root
        # while head or rights:
        #     if head:
        #         ans.append(head.val)
        #         if head.right:
        #             rights.append(head.right)
        #         head = head.left
        #     else:
        #         head = rights.pop()
        # return ans
        ans = []
        def preorder(root):
            if root == None:
                return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans




        
