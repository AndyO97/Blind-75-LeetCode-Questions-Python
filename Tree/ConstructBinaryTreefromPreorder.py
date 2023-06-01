# Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder goes from left to right, starting from the level on the top of the tree
# Left to right toppest level, then left to right next level

# inorder starts from the leftmost branch and goes to the root, then the next leftmost branch and goes to one level lower
#  the root and so on.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # Recursive solution
        # Check that the inorder array is not empty or null, otherwise skip
        if inorder:   
            # Find index of root node within in-order traversal
            index = inorder.index(preorder.pop(0)) #preorder[0] has the root, or left or right to the root (depending on the iterative call we are in)
            root = TreeNode(inorder[index]) #Set the root
            
            # Recursively generate left subtree starting from 
            # 0th index to root index within in-order traversal
            root.left = self.buildTree(preorder, inorder[:index]) # We know that we are dealing with the left section (0 to index)
            
            # Recursively generate right subtree starting from 
            # next of root index till last index
            root.right = self.buildTree(preorder, inorder[index+1:]) # We know that we are dealing with the right section (index to end)
            return root