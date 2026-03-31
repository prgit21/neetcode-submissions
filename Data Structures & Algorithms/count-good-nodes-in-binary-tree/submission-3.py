# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # use helper cus we need to compress state
        #invariant is -> we need to count all good nodes, which have a value greater than the max seen on path so far

        def dfs(maxv,node):
            # base case of if no node anymore -> reached end
            if not node:
                return 0
            if maxv <=node.val:
                good=1
            else:
                good =0
            # compute maxVal
            maxv=max(maxv,node.val)
            return good + dfs(maxv,node.left) + dfs(maxv,node.right)

            
        return dfs(root.val,root)