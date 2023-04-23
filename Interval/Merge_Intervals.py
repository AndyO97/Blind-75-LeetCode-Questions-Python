# Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping 
# intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# https://medium.com/tech-life-fun/leet-code-56-merge-intervals-explained-python3-solution-89b3297e81a1

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort all intervals so we can merge them in order
        intervals = sorted(intervals, key=lambda x:x[0])
        #Initialize array where we will store the merged intervals
        ret = []
        for i in intervals:
            newInterval = i
            #compare with the last one in ret
            if ret:
                #If the upper limit of the last interval stored in ret is bigger than the lower limit of the current interval
                #merge and then replace the last one in ret
                if ret[-1][1] >= i[0]: 
                    # First pop it
                    newInterval = ret.pop()
                    # Then check if the upper limit of the last interval is bigger than the upper limit of teh current interval,
                    # If yes, Update the upper limit
                    if i[1] > newInterval[1]:
                        newInterval[1] = i[1]      
            ret.append(newInterval)
        return ret

    #Alternate solution but slower performance:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     ans=[]
    #     n = len(intervals)
    #     i = 1
    #     intervals = sorted(intervals, key=lambda x:x[0])

    #     if n == 0:
    #         return ans
        
    #     start = intervals[0][0]
    #     end = intervals[0][1]

    #     while(i < n):
    #         if( intervals[i][0] <= end):
    #             #end = intervals[i][1]
    #             #start = min(start, intervals[i][0])
    #             end = max(end, intervals[i][1])
    #         else:
    #             ans.append([start, end])
    #             start = intervals[i][0]
    #             end = intervals[i][1]
    #         i+=1

    #     ans.append([start, end])

    #     return ans
