class Solution:
    def trap(self, height: List[int]) -> int:
        # rain = 0
        # left = 0
        # for right in range(len(height)):
        #     if height[right] >= height[left]:
        #         bottleneck = height[left]
        #         left += 1
        #         while left < right:
        #             rain += bottleneck - height[left]
        #             left += 1
        # if height[-1] >= height[left]:
        #     bottleneck = min(height[left], height[-1])
        #     left += 1
        #     while left < right:
        #         rain += bottleneck - height[left]
        #         left += 1
        # return rain
        
        mono = []
        rain = 0
        for h in height:
            # print(mono, rain)
            while mono and mono[0] <= h:
                rain += min(h, mono[0]) - mono.pop()
            mono.append(h)
        while mono:
            localMini = mono.pop()
            while mono and mono[-1] < localMini:
                rain += localMini - mono.pop()
                
        return rain