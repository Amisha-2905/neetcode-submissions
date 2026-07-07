class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans = ''
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1

        if i != len(word1):
            while i < len(word1):
                ans += word1[i]
                i += 1
        elif j != len(word2):
            while j < len(word2):
                ans += word2[j]
                j += 1
        return ans

        