# Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# https://leetcode.com/problems/same-tree/solutions/32729/shortest-simplest-python/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Most easy to understand solution:

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both are null, we have reached the end, then return true
        if p is None and q is None:
            return True
        # If only one is null, the tree is not the same
        elif p is None or q is None:
            return False
        #If the current heads are equal, we can continue going down the tree. Otherwise return false
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
            
# Most elegant and faster solution:

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If p and q are not null, only return true if the heads are equal and if going down the tree, the heads keep to be equal
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Else check if they are the same object (null)
        return p is q