# Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right =0, len(height)-1
        result = 0
        
        while left < right:
            #Obtain the area of the container with current left and right indeces
            water = (right-left) * min(height[left], height[right])
            #If the result is greater than the previous result, update it
            if water > result:
                result = water
            #If the right has a greater value, try with the left
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return result