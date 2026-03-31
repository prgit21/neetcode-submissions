# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #core - > only the trees in the right most at every level should be appended to a res list
        #inv-> use bfs + qto scan at every level, at every level store only the last element appended to the queue
        #state -> res, levels to hold intermediate values and k len at every level
        
        q=deque()
        q.append(root)
        res=[]

        while q:
            k=len(q)
            levels=[]

            for _ in range(k):
                #pop a queue element for every item at that level and append it to intermediate state levels
                node=q.popleft()
                if node:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levels:
                    res.append(levels[-1])
        return res

