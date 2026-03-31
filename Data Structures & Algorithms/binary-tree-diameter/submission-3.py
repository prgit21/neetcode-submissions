# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #need to check length of path passing through every node
        #tree atleast has one node
        res=0       #maintain a global res which is max diam seen so far
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)

            res=max(res,left+right)     #compute the res at every ecursion per node

            return 1+max(left,right)    #return only the max height of each path


        dfs(root)
        return res