
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # need to check if tree has a subroot inside it 
        #check edge cases- > when nly root exists, when only subroot exists

        if root and not subRoot:
            return True
        
        if not root:
            return False
        
        # do dfs to check if curremt node has subtree

        if self.dfs(root,subRoot):
            return True
        
        #explore for all other nodes in tree
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



    def dfs(self,rt,sub):
        # check if its a subtree,
        #check for if both exist and define base case

        if not rt and not sub:
            return True
        
        if not rt and sub or rt and not sub:
            return False
        if rt.val!= sub.val:
            return False

        #run dfs in parallel 
        return self.dfs(rt.right,sub.right) and self.dfs(rt.left,sub.left)