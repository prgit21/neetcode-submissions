# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #need to see if left or right is longer
        #prefer doing dfs or calling function recursively
        # at every recursion update state of maxDepth
        #assumption -> can be 0 nodes, if 0 nodes return 0, but recursion may go overbouund by 1
        #what state -> curr len, and max len, so dfs better
        maxH=0
        if not root:
            return 0

        lef=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        maxH=1+max(lef,right)

        return maxH