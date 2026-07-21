class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        
        
        n = len(gas)
        memo = [gas[i] - cost[i] for i in range(n)]

        balance = 0
        ans = 0
        for i in range(n):
            balance += memo[i]
            if balance < 0:
                balance = 0
                ans = (i + 1) % n
            
        return ans
       
        
        