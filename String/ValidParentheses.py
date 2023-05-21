# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '{':'}','[':']'}
        stack = []
        #Traverse every element in the string
        for i in s:
            # Check if it is an opening bracket and if yes, append it to the stack
            if i in d:
                stack.append(i)
            # Else, check if the stack is empty(meaning no matching left bracket) or if the popped element's value (closing bracket) doesn't match the current element
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
            
        # Lastly, check if the stack still contains unmatched opening brackets
        return len(stack) == 0 # 3
	


