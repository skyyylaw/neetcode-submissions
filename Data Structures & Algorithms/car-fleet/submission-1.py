class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        memo = [ (position[i], speed[i]) for i in range(len(position))]
        memo.sort()
        memo = [(target - p)/s for p, s in memo]
        mono = []
        for eta in memo:
            if not mono:
                mono.append(eta)
            else:
                if eta >= mono[-1]:
                    mono[-1] = eta
                else:
                    mono.append(eta)
        return len(mono)