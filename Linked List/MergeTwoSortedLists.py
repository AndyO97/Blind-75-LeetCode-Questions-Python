# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node will be used to return the head of the response
        dummy = curr = ListNode()
        # Traverse both the lists until either one or both are exhausted
        while list1 and list2:
            #If the current value of the list1 node is smaller than the value of the current list2 node, 
            # we append the list1 node to our curr’s next pointer, and move to the next node in list1.
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            # Else, if the value in list2 is smaller,
            # we append the list2 node to our curr’s next pointer, and move to the next node in list2, 
            else:
                curr.next = list2
                list2 = list2.next
            # Then, we move the curr node to it’s next node.
            curr = curr.next
                    
        # Then point the next pointer of our curr node to the remaining list
        curr.next = list1 or list2

        # Finally, return the next node to the dummy node which is where the new merged list starts  
        return dummy.next