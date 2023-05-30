#Subtree of Another Tree

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of 
# subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered 
# as a subtree of itself.

 
# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

################################Solution###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # First check if the root is not null
        if not root: 
            return False
        # Check if both trees are the same, if yes return treu
        if self.isSameTree(root, subRoot): 
            return True
        # Then, try with the left section of the subroot and with the right section (recursively)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # Function to check if trees p and q are the same (recursively)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If not p and q, check if both are null
        return p is q