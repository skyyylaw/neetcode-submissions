class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while mono and temperatures[mono[-1]] < t:
                temp = mono.pop()
                res[temp] = i - temp
            mono.append(i)
        return res

