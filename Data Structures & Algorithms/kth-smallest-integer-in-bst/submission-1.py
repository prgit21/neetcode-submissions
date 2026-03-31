
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #seems like dfs to me
        #given its bst, start inorder 
        #iterate k number of times over node and return the kth element
        # CONSIDER edge case where k > tot num of nodes -> return smallest then

        arr=[]

        def dfs(node):
            if not node:
                return

            dfs(node.left)            
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k-1]