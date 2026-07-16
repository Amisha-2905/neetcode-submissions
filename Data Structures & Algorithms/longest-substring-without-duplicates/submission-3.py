class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        curr = 0
        start = 0
        keep = [-1] * 128
        for i, char in enumerate(s):
            if keep[ord(char)] < start:
                curr += 1
                keep[ord(char)] = i
            else:
                if curr > ans:
                    ans = curr
                start = keep[ord(char)] + 1
                keep[ord(char)] = i
                curr = i - start + 1
            
        if curr > ans:
            ans = curr
        return ans