from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_1 = len(s1)
        len_2 = len(s2)
        if len_1 > len_2:
            return False
        
        count_1 = Counter(s1)
        for i in range(0, len_2 - len_1 + 1):
            count_2 = Counter(s2[i:i+len_1])
            if count_1 == count_2:
                print (s2[i:i+len_1])
                return True
        return False
