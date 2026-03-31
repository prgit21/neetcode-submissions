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
            return None
        
        if max(p.val,q.val)<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val)>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

