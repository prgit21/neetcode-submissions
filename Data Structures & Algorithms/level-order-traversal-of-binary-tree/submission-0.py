# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #do bfs and scan levels
        #init q, append q
        #while q exists iteratively pass through levels for k=len(q) to be calc at every iter
        #check if node, pop left and store node.val in res
        #if node then move left and right
        #after each pass store in res and continue

        res=[]
        q=deque()
        q.append(root)

        while q:
            levels=[]
            k=len(q)
            for _ in range (k):
                node= q.popleft()
                if node:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levels:
                    res.append(levels)
        return res
