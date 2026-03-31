# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if self.dfs(root,subRoot):
            return True

        if root is None:
            return False
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    def dfs(self,rt,sub):
            if not rt and sub:
                return False
            if rt and not sub:
                return False
            
            if not rt and not sub:
                return True
            
            if rt.val!=sub.val:
                return False

            return self.dfs(rt.left,sub.left) and self.dfs(rt.right,sub.right)




        
