# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #do dfs on both trees in parallel
        #check if p and q exist and if p.val =q.val 
        #then proceed to recursively iterate p.left and q.left and then p.right and q.right
        #if val is equivalant or both are null return true
        #else false

        if not p and not q:
            return True
        
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False