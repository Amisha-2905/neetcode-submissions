class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            temp = (n >> i) & 1
            ans += temp
        return ans