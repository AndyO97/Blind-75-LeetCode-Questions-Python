# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        n = len(intervals)
        i = 0

        # Check for interval[i] < newInterval
        # While the interval are lower than the newInterval, append the intervals normally
        while(i < n and intervals[i][1] < newInterval[0]):
            ans.append(intervals[i])
            i += 1

        #ans = intervals[:i]

        # Check for interval[i]'s that are in between newInterval
        # Build the new newInterval

        while(i < n and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
            
        ans.append(newInterval)

        #Append the remaining intervals
        while(i < n):
           ans.append(intervals[i])
           i += 1

        return ans