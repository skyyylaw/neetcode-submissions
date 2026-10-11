class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftBound = {}
        rightBound = {}

        monoIncrease = []

        ans = 0

        for i in range(len(heights)):
            while monoIncrease and heights[monoIncrease[-1]] > heights[i]:
                currIndex = monoIncrease.pop()
                area = 0
                height = heights[currIndex]
                if not monoIncrease:
                    # print("no left bound")
                    area = (currIndex + 1) * height
                else:
                    # print(f"left bound is {monoIncrease[-1]+1} and rightBound is {currIndex}")
                    ans = (currIndex - monoIncrease[-1]) * height
                
                ans = max(ans, area)

            monoIncrease.append(i)
        
        while monoIncrease:
            # print("no right bound")
            currIndex = monoIncrease.pop()
            area = 0
            height = heights[currIndex]
            if not monoIncrease:
                # print("no leftBound")
                area = (currIndex + 1) * height
            else:
                # print(f"left bound is {monoIncrease[-1]+1} and rightBound is {currIndex}")
                area = (len(heights) - monoIncrease[-1] - 1) * height
            ans = max(ans, area)


        # 0 1 2 3 4 = 5
        return ans



