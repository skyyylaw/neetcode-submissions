class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftBound = {}
        rightBound = {}

        monoIncrease = []

        ans = 0

        for i in range(len(heights)):
            while monoIncrease and heights[monoIncrease[-1]] > heights[i]:
                currIndex = monoIncrease.pop()

                # print("find left bound")
                while monoIncrease and heights[monoIncrease[-1]] == heights[currIndex]:
                    monoIncrease.pop()

                if not monoIncrease:
                    # print("left bound is 0")
                    ans = max(ans, (currIndex+1) * heights[currIndex])
                else:
                    # print(f"left bound is {monoIncrease[-1]} and rightBound is {i}")
                    ans = max(ans, (i - monoIncrease[-1] - 1) * heights[currIndex])
            
            monoIncrease.append(i)
        
        while monoIncrease:
            # print("left bound is len(heights)-1")
            currIndex = monoIncrease.pop()
            while monoIncrease and heights[monoIncrease[-1]] == heights[currIndex]:
                monoIncrease.pop()

            if not monoIncrease:
                # print("left bound is 0")
                ans = max(ans, (len(heights) - currIndex) * heights[currIndex])
            else:
                # print("right bound is len(heights)-1")
                ans = max(ans, (len(heights) - 1 - monoIncrease[-1]) * heights[currIndex])
        
        return ans