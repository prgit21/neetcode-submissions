# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #go to root
        #then go to left side of root and recursively swap left and right pointer for heoght of tree
        #go to right side of root and recursively swap lefy and right pointer along height of tree
        #swap whole sub tree to left and right of node
        
        if not root:
            return None
            
        tmp=root.left
        root.left=root.right
        root.right=tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root