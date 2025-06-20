# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def inorder(root,previousPath):
            if root == None:
                return
            previousPath += str(root.val) + "$"
            inorder(root.left,previousPath)
            inorder(root.right,previousPath)
            if root.left == None and root.right == None:
                ans.append(previousPath[:-1]) # to remove "$" and the end of the path since for the seek of removing extra "->" path indicator in final path. 
                # removing 1->2->3-> case instead of 1->2->3
            
        inorder(root,"")
        for i in range(len(ans)):
            subAns = ans[i].split("$")
            ans[i] = "->".join((subAns))
        return ans

        
