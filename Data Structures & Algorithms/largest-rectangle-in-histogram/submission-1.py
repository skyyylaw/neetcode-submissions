class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftBound = {}
        rightBound = {}

        mono = []
        
        for i in range(len(heights)):
            while  mono and heights[i] < heights[mono[-1]]:
                rightBound[mono.pop()] = i
            mono.append(i)
        while mono:
            rightBound[mono.pop()] = len(heights)
        
        for i in range(len(heights) - 1, -1, -1):
            while mono and heights[i] < heights[mono[-1]]:
                leftBound[mono.pop()] = i
            mono.append(i)
        while mono:
            leftBound[mono.pop()] = -1

        ans = 0
        for i in range(len(heights)):
            ans = max(ans, (rightBound[i] - leftBound[i] - 1) * heights[i])
        
        return ans