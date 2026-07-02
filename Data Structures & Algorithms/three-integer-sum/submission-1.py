class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]
            while j < k:
                curr_sum = nums[j] + nums[k]
                if target == curr_sum:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif target > curr_sum:
                    j += 1
                else:
                    k -= 1
        return ans

