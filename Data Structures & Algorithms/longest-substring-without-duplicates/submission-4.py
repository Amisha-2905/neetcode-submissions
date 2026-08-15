class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        keep = [-1] * 128
        start = 0
        ans = 0
        for i in range(len(s)):
            c = s[i]

            if keep[ord(c)] >= start:
                start = keep[ord(c)] + 1

            keep[ord(c)] = i
            ans = max(ans, i - start + 1)

        return ans