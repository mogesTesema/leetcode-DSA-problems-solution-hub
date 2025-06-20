# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.found = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node,subNode):
            if node ==None and subNode == None:
                return True
            elif node == None and subNode != None:
                return False
            elif node != None and subNode == None:
                return False
            if node.val != subNode.val:
                return False
            return check(node.left,subNode.left) and check(node.right, subNode.right)
            
        def preorder(node,subNode):
            if node == None:
                return
            if node.val == subNode.val:
                if check(node,subNode):
                    self.found = True
                    return
                    
            preorder(node.left,subNode)
            preorder(node.right,subNode)
        preorder(root,subRoot)
        return self.found

