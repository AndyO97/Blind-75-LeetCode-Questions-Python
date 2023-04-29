# Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# About heapq
# heapq is used to achieve O(1) complexity to get smallest element out of a bunch elements. 
# A detail to know for Python3 heaqp is: when I heappush a tuple, by default, tuple[0] will be used to compare with existing tuples’ tuple[0],
# if there is equal pair, tuple[1] will be used.

# Heaps are binary trees for which every parent node has a value less than or equal to any of its children. 
# This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero.


# heapq.heappush(heap, item)
#     Push the value item onto the heap, maintaining the heap invariant.

# heapq.heappop(heap)
#     Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. 
#     To access the smallest item without popping it, use heap[0].


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Initialize the ListNode and have ret pointing the head, for later returning it as the answer
        ret = ListNode()
        # p will be used to build the merged linkedList
        p = ret
        # h will contain the heap
        h = []
        # Start the counter on 0
        # Counter needs to be used for not raising errors of type "#TypeError: '<' not supported"
        # heapq is capable of dealing with tuples. 
        # It is actually necessary to use a 3-element tuple because if the node values are equal, 
        # ListNodes cannot be compared as written.
        # heapq will pick the first field/key by default for comparing. If the first fields are equal, it will compare the second fields.
        cnt = 0
        for lst in lists:
            if lst:
                # Push the element to the priority heap
                heapq.heappush(h, (lst.val, cnt, lst))
                # Add counter
                cnt += 1

        #After adding all the heads of the linkedLists to the heap a while loop to begin adding them orderly
        
        #While there are elements in the heap        
        while(len(h)):
            smallestPnt = heapq.heappop(h)[2] #Get the smallest element of the heap and use index 2 to get the actual pointer
            p.next = smallestPnt    #Set the next element in the linkedlist
            p = p.next              #Point to the next element 
            if smallestPnt.next:    #Check if the list popped has more elements and if yes, add the next element back to the priority heap
                heapq.heappush(h, (smallestPnt.next.val, cnt, smallestPnt.next))
                cnt += 1    #Update counter
        return ret.next