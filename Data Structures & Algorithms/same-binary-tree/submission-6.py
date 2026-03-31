# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if p or q exist indpenednetly
        #check if p and q are none

        if p and not q or not p and q:
            return False
        
        if not p and not q:
            return True
        
        if p.val!=q.val:
            return False

        # do dfs in parallel on each of the,

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
