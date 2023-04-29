# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# https://redquark.org/leetcode/0019-remove-nth-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Two Pointer Technique

# This technique is used to solve multiple linked list problems. We use two pointers, slow and fast. The fast pointer sometimes :

#     Moves faster than the slow pointer (two steps at a time, for example)
#     Moves ahead of the slow pointer with same speed (n steps ahead, for example)

# This problem requires the usage of the two pointer technique where both pointers move with same speed but the fast pointer is n steps ahead of the slow pointer.


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, pointing to the head of the linked list.
        slow = head
        fast = head
        # Move fast pointer n steps ahead
        for i in range(0, n):
            if fast.next is None:
                #Special case!!!! 
                # If n is equal to the number of nodes, delete the head node
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next

        # Move both slow and fast one step at a time until fast reaches to the end. 
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # When the fast pointer reaches the end, the slow pointer will be n steps behind the end of the list.
        # At this point, remove the node and link it to the next node of the current node.
        if slow.next is not None:
            slow.next = slow.next.next
        return head