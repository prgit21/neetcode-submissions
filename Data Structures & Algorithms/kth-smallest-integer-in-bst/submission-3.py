
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #invariant -> an element which is nth inorder traversal is the right ans
        # start inorder traversal, compute count and check if count is == k , if so update ans and exit early

        count,ans=0,None
        def dfs(node):
            nonlocal count , ans 

            if not node or ans is not None:
                return
            
            dfs(node.left)
            count+=1

            if count==k:
                ans=node.val
            dfs(node.right)

        dfs(root)
        return ans

