# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #dfs again
        #traverse down tree and at each node run reccursivley to see if it is subtree
        #on success break recursion and if we pass all and get no sub tree then return false

        if not subRoot:
            return True
        if not root:
            return False

        
        if self.isEqual(root,subRoot):            
            return True
        else:
            return (self.isSubtree (root.right,subRoot) or self.isSubtree(root.left,subRoot))

    def isEqual(self,root,sub):
        if not root and not sub:
            return True

        if root and sub and root.val == sub.val:
            return self.isEqual(root.left , sub.left) and self.isEqual(root.right,sub.right)
        else:
            return False
        
        