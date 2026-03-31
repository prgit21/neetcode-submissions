# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #need to do dfs
        #scan path from root
        #if root val greater than node x , and lesser than maxVal valid else invalid
        
        def dfs(root,maxVal):
            if not root:
                return 0
            good =1 if root.val>=maxVal else 0
            new_max=max(maxVal,root.val)

            return good + dfs(root.left,new_max)+dfs(root.right,new_max)
            
        return dfs(root,root.val)
            

            
            