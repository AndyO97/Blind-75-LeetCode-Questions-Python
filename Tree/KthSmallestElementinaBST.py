# Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values 
# of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Count array for storing the ordered elements of the BST
        count = []
        # Call the recursive helper function to append the elements to count
        self.helper(root, count)
        # Return the Kth Smallest Element (-1 because 1-indexed)
        return count[k-1]
        
    def helper(self, node, count):
        # if null, exit be returning
        if not node:
            return
        
        # Continue calling the left the recursive function on the left node (to get the elements in order)
        self.helper(node.left, count)
        # Then append the current node's value
        count.append(node.val)
        # Then tranverse the elements on the right node.
        self.helper(node.right, count)