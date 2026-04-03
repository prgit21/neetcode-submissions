# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #use helper to compress state per recursion call 

        def dfs(maxVal,node):
            #check empty node
            if not node:
                return 0
            #count good nodes

            if maxVal <= node.val:
                good=1
            else:
                good=0
            
            maxVal=max(maxVal,node.val)

            return good+dfs(maxVal,node.left)+dfs(maxVal,node.right)
        
        return dfs(root.val,root)