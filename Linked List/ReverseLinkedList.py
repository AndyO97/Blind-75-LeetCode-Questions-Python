# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example:
# 1 -> 2 -> 3 -> 4 -> 5
# Result:
# 5 -> 4 -> 3 -> 2 -> 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while(current is not None):
            # Get the next node
            next = current.next
            # Set to the current node the previous node
            current.next = prev
            # Set the prevoious and current for the next iteration
            prev = current
            current = next
        return prev