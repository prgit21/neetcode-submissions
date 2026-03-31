# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # run dfs recursively at each node
        #do left and then right 
        #at left of root node check if node.left < node.val and to its right node.val < node.right        
        #edge case deeper than 1 level -> need to maintain some upper and lower bound,
        # upper bound for left of root is root itsefl , for lower bound, update value based on what the parent is? 
        #for right side lower bound is root and upper bound is parent value        
        #from every node return a global bool flag of valid invalid and if False quit and return resp, also pass upper and lower bound on each side of tree

        def dfs (node,lower,upper):
            if not node:
                return True
            if not (lower<node.val<upper):
                return False
            return dfs(node.left,lower,node.val) and dfs(node.right,node.val,upper)
        
        return dfs(root,float('-inf'),float('inf'))