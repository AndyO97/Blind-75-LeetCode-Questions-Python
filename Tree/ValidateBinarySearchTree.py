# Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursive function that will be used
        def valid(node, left, right):
            # If there is no node, return true as there is nothing to check
            if not node:
                return True
            # If the value of the current node is not greater than the left and less than the right, return false
            if not ( left<node.val and node.val<right ):
                return False
            
            # Continue veryfing the left and right of the current node (return and and of both recursive returns)
            return (valid(node.left, left, node.val) and #Update the middle limit with the current value (node.val)
                    valid(node.right, node.val, right))
        
        # Make the initial call 
        return valid(root, float(-inf), float(inf))