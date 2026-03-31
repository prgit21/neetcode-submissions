# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #invariant -> if every node structure is same on either side then tree is same
        #start with dfs to scan one side and compare every node then root then the right side
        #break if wrong anywehrew

        if p and not q:
            #if q doesnt exist and p exists 
            return False
        
        if not p and q:
            #if p doesnt exist and q exists
            return False
        if not p and not q:
            return True
        
        if p.val!=q.val:
            return False

            #if the initial values are same iteratively scan each side and compare values
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 
        