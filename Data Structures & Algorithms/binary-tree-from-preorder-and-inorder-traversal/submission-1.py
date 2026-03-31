# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # identify root and left hand side of tree from preorder and inorder lists
        # create root node using inorder and call it mid
        #build left tree from index 0 preorder t o mid+1 and to mid of inorder
        #build right tree from mid+1 of preorder till end and end of preorder

        if not preorder and not inorder:
            return None
        
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid +1:],inorder[mid+1:])

        return root

