class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            l = int(details[i][-4])
            if l > 6:
                count += 1
            if l == 6:
                r = int(details[i][-3])
                if r >= 1:
                    count += 1
        return count