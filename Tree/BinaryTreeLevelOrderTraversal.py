#Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return root
        
        # Generate queue and append root to queue
        queue = []
        return_list = []
        queue.append(root)
        #while there are nodes in the queue, 
        while len(queue) > 0:
            ans = []
            l = len(queue)
            #iterate through the number of nodes in the queue (this is the number of nodes in the next level)
            for l in range(l):
                #pop queue(0), add queue(0).val to current ans list and append queue(0)'s children to queue
                node = queue.pop(0)
                ans.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            #append ans to final_list and reset ans (on the next iteration)
            return_list.append(ans)
        return return_list