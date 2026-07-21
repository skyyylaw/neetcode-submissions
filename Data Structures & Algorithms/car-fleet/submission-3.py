class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        memo = [ (position[i], speed[i]) for i in range(len(position))]
        memo.sort()
        # print(memo)
        memo = [(target - p)/s for p, s in memo]
        mono = []
        # print(memo)
        for eta in memo:
            # print(mono)
            if not mono:
                mono.append(eta)
            else:
                while mono and eta >= mono[-1]:
                    mono.pop()
                mono.append(eta)
        return len(mono)