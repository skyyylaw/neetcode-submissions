class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        i = len(position)-1
        while i >= 0:
            res += 1
            leaderTimeToDest = (target - position[i]) / speed[i]
            j = i - 1
            while j >= 0 and ((target - position[j]) / speed[j]) <= leaderTimeToDest:
                j -= 1
            i = j - 1
        return res