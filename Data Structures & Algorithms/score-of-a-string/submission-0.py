class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            l = ord(s[i])
            r = ord(s[i + 1])
            temp = max(l - r, r - l)
            ans += temp
        return ans