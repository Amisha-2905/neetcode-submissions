class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}

        for string in s:
            count[string] = count.get(string, 0) + 1

        max_odd = 1
        min_even = 100

        for key, value in count.items():
            if value % 2 != 0:
                if value > max_odd:
                    max_odd = value
            else:
                if value < min_even:
                    min_even = value
        
        return max_odd - min_even
                
