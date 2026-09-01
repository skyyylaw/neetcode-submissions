class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {
            5: 0,
            10: 0,
            20: 0,
        }
        for b in bills:
            register[b] += 1
            
            change = b - 5
            for amount in [20, 10, 5]:
                while register[amount] > 0 and change >= amount:
                    register[amount] -= 1
                    change -= amount
            if change != 0:
                return False
                
        return True