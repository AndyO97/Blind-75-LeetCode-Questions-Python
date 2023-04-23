#Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals 
# you need to remove to make the rest of the intervals non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        # if size 0, return 0
        if size<=1: 
            return 0
        # Sort intervals based on the upper limit, 
        # Therefore the upper limit can be used to compare the previous interval and identify if there is an overlap
        intervals.sort(key=lambda x: x[1])
        # Get the first upper limit
        previous_end = intervals[0][1]
        # Initialize the number of intervals that need to be removed (answer to be returned)
        res = 0
        # Start with the second interval 
        for i in range(1,size):
            start, end = intervals[i]
            # If the lower limit of the current interval is greater than the previous end (there is no overlap)
            # Update previous end
            if start>=previous_end:
                previous_end=end
            # Else, add one to the number of intervals we need to remove
            else:
                res+=1
        return res