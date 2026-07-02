class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, num in enumerate(nums):
            dict_nums[num] =  i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_nums and dict_nums[diff] != i:
                return [i, dict_nums[diff]]
        return []