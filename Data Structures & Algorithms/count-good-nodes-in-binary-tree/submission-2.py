# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #do dfs,create a maxValue
        #do dfs at each node recusrively        
        #at each node updatw max Value and compare it with root
        # if root > node val and max val< node val, then valid

        def dfs(node,maxVal):
            if not node:
                return 0
            if node.val >= maxVal :
                good =1
            else: 
                good=0
            maxVal=max(maxVal,node.val)

            return good+dfs(node.left,maxVal)+dfs(node.right,maxVal)
        return dfs(root,root.val)