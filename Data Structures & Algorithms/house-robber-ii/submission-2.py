from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def solve(i, rob_1):
            if i >= len(nums):
                return 0
            if i == 0:
                rob = nums[i] + solve(i + 2, 1)
                skip = solve(i + 1, 0)
                return max(rob, skip)
            elif i == len(nums) - 1:
                if rob_1 == 1:
                    return 0
                else:
                    rob = nums[i] + solve(i + 2, 0)
                    skip = solve(i + 1, 0)
            rob = nums[i] + solve(i + 2, rob_1)
            skip = solve(i + 1, rob_1)

            return max(rob, skip)

        return solve(0, 0)