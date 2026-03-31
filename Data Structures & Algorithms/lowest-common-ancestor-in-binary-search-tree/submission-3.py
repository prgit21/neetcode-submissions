# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if root > p &q then move LEFT
        #if root < p & q move right
        #if root == p or q, reutrn whatever matches 
        #if root < p and q !<root or root<q and q !< root -> return current node

        if not root:
            return root
        
        if root.val > p.val and (root.val> q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        if root.val == p.val:
            return root

        elif root.val == q.val:
            return root
        
        if (root.val < p.val and root.val >q.val ) or (root.val > p.val and root.val < q.val):
            return root