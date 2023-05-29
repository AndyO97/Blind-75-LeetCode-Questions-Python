# Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or 
# transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so 
# please be creative and come up with different approaches yourself.

 

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:

# Input: root = []
# Output: []


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        # Recursively build string with contents of tree
        # Separate each element in the string with a comma
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}" 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        #Use split to send as param a list of the elements of the tree
        return self.deserialize_list(data.split(","))
    
    def deserialize_list(self, nums: List[str]):
        # Pop the first element of the array
        val = nums.pop(0)
        # If there is nothing else we have finished deserializing the string
        if not val:
            return None

        # Set the root to the current popped value
        root = TreeNode(val)
        # Set the left and right node by recursively calling this same function
        root.left = self.deserialize_list(nums)
        root.right = self.deserialize_list(nums)

        return root
        