# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        models = dict()
        
        def preorder(root):
            if root == None:
                return
            if root.val in models:
                models[root.val] += 1
            else:
                models[root.val] = 1
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        print(models)
        models = sorted(models.items(),key= lambda item: item[1],
        reverse =True)
        print(models)
        maxOccure = models[0][1]
        ans = []
        models = dict(models)
        for key, value in models.items():
            #print(f"key:{key} and value: {value}")
            if value == maxOccure:
                ans.append(key)
            else:
                break
        return ans


