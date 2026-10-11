class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twen = 0

        for b in bills:
            match b:
                case 5:
                    five += 1
                case 10:
                    ten += 1
                case twen:
                    twen += 1
            
            change = b - 5

            while five > 0 and change >= 5:
                five -= 1
                change -= 5
            
            while ten > 0 and change >= 10:
                five -= 1
                change -= 10
            
            while twen > 0 and change >= 20:
                five -= 1
                change -= 20
                
            if change != 0:
                return False
                
        return True