# Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# SOLUTION 
# 1. Split the lists into two halves using slow and fast pointers.
# 2. The node next to where the slow pointer is pointing will be the head of the second list just after splitting.
# 3. Reverse the second list.
# 4. Merge the two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Initiliaize slow and fast
        # However, do not modify the pointer of head
        slow = head
        fast = head.next
        
        # Split the linked list in 2
        # When the fast array reaches the end, the slow node will contain the end of the first list and will be pointing to be begining of the second list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        #reverse second list
        second = slow.next  #head of second list
        slow.next = None #pointing tail of first list to null
        prev = None
        
        #while for reversing the second list
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
            
        #prev will end having the head of the reversed linked list
            
        #merge two halves
        first, second = head, prev
        
        while second:
            #Get the next nodes of both lists to be assigned
            nextList1 = first.next
            nextList2 = second.next
            
            # Update the corresponding next nodes of both lists
            # However, in this process both lists are turning into one
            first.next = second 
            second.next = nextList1

            #Move to the next node on both list for being ready for the next iteration of the loop
            first = nextList1
            second = nextList2