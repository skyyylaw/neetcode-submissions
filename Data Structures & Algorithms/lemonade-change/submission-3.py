class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twen = 0

        for b in bills:
            
            change = b - 5

            match b:
                case 5:
                    five += 1
                case 10:
                    ten += 1
                case 20:
                    twen += 1
            
            while twen > 0 and change >= 20:
                twen -= 1
                change -= 20
            
            while ten > 0 and change >= 10:
                ten -= 1
                change -= 10

            while five > 0 and change >= 5:
                five -= 1
                change -= 5
            
           
            
            
                
            if change != 0:
                return False
                
        return True