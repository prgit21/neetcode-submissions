# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do bfs only on right side of tree
        # at every level append only the node in the last position of the list to res

        #traverse only to right of node, and every node under root, traverse only to the right

        q= deque()
        q.append(root)
        res=[]
        flat=[]

        if not root:
            return []

        while q:
            levels=[]
            k=len(q)

            for _ in range (k):                
                node=q.popleft()
                if node:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            
            if levels:
                    res.append(levels[-1])
        return res
        
                
        




        