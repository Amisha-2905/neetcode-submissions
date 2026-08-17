class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for num in nums:
            if num != 1:
                curr = 0
            else:
                curr += 1
            ans = max(curr, ans)
        return ans