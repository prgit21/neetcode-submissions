# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:                
        
        #can do dfs or bfs
        #prefer to do dfs
        #find max height from root, if max height from root difference > 1 then not balance
        #but domt find only from root, computte max height from every single node elem
        #state to be computed and passed to parent is max height of parent from that node
        #dfs shape ->(node) -> we dont need to remember the height outside each recursion as we just need to compare


        def dfs(node):
            #dfs ret -> (isBal,height) to parent at every single node
            #check base case
            if not node:
                return (True,0)
            # now need to find leftheight,and leftbal
            lbal,lh=dfs(node.left)
            rbal,rh=dfs(node.right)

            #compute whatever state u need -> here it is if its balanced, and height
            balanced=(
                (lbal and rbal) and (abs(lh-rh)<=1)
            )

            height=1+max(lh,rh)

            return (balanced,height)
        
        return dfs(root)[0]