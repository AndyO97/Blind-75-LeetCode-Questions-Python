# Binary Tree Maximum Path Sum

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
# A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 
# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Concept:

# Every single node in the original tree could be the "root" of the max path.
# For every one of these "roots", we could add the MPS on the left, the MPS on the right, neither, or both to get the overall max path (MP).
# MPS: max path of the subtree created by following node.left or node.right.
# At the end, we return the max of EITHER just the root, the root and the max path left subtree, or the root and the max path right subtree.
# Why not root and both left and right subtree? If the root ISN'T the actual root, it'll be in either the left or right subtree of the actual root. Since we want a single path, the path can't split, so it needs to take exactly one road, left or right.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Init the property in the class that will hold the answer to minus infinity
        self.ans = float('-inf')
        # Call the recursive function
        self.helper(root)
        # Finally return the answer
        return self.ans 
        
    # Helper function will return the maximum path sum for root node    
    def helper(self, root):
        # Check that the head/root is not null. If it is, return 0
        if not root:
            return 0
        # Get the maximum path sum for left and right
        left, right = self.helper(root.left), self.helper(root.right)
        # Then update the class answer if sum of the current path is greater than the previous one.
        self.ans = max(self.ans, root.val + left + right) # Only will be kept if the current root is used as the root of the final path
        # Finally, return the maximum path sum for the current root
        return max(root.val + max(left, right), 0)  #In this case we can either go left or right