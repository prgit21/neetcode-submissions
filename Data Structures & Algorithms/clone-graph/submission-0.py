"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map={}

        if not node:
            return None
        def dfs(rnode)->'Node':
            # if node exists in copied
            if rnode in node_map:
                return node_map[rnode]
            #if not append 
            copied=Node(rnode.val)
            # append to map
            node_map[rnode]=copied
            # recursively attach neighbors of node to its copied node
            for nbrs in rnode.neighbors:
                copied.neighbors.append(dfs(nbrs))
            return copied

        return dfs(node)