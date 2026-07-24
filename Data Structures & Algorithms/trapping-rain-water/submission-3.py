class Solution:
    def trap(self, height: List[int]) -> int:
        
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