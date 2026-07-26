from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def solve(i):
            if i >= len(nums):
                return 0

            rob = nums[i] + solve(i + 2)
            skip = solve(i + 1)

            return max(rob, skip)

        return solve(0)