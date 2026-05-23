class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        area = 0
        j=len(heights) - 1
        maxarea=0
        while i < j:
            if heights[j]<heights[i]:
                area = (j-i)*heights[j]
                maxarea = max(area,maxarea)
                j -=1
            elif heights[j]>heights[i]:
                area = (j-i)*heights[i]
                maxarea = max(area,maxarea)
                i +=1
            else:
                area = (j-i)*heights[j]
                maxarea = max(area,maxarea)
                j-=1
        return maxarea


