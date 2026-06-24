class Solution:
    def isUgly(self, n: int) -> bool:
        if n in [1, 2, 3, 5]:
            return True
        
        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            if n % 2 == 0:
                n = n / 2
            if n % 3 == 0:
                n = n / 3
            if n % 5 == 0:
                n = n / 5
        
        if int(n) == 1:
            return True

        return False 