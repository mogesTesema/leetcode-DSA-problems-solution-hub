# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root, data):
            if root is None:
                return TreeNode(data)
            if data < root.val:
                root.left = insert(root.left, data)
                return root
            if data > root.val:
                root.right = insert(root.right, data)
                return root
        return insert(root,val)
        # def insertInto(root):
        #     if root == None: 
        #         return
        #     if val > root.val:
        #         right = insertInto(root.right)
        #     else:
        #         left = insertInto(root.left)
        #     if root.left == None and val < root.val:
        #         root.left = TreeNode(val)
        #         return
        #     if root.right == None and val > root.val:
        #         root.right = TreeNode(val)
        #         return
        # if root == None: return TreeNode(val)
        # insertInto(root)
        # return root


        
