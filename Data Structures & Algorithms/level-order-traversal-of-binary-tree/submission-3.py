# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #int -> since level order use bfs
        #invariant-> at every level, pick all nodes and create a sublist , scan one level at a time
        #use an empty queue to append nodes at each level and then append them to a list

        if not root:
            return []

        q=deque()
        q.append(root)
        res=[]
        while q:
            ints=[]
            k=len(q)

            for _ in range(k):
                node=q.popleft()
                
                if node:
                    ints.append(node.val)            
                    q.append(node.left)
                    q.append(node.right)
            if ints:
                    res.append(ints)
        return res