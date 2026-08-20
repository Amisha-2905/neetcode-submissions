class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 0
        j = len(nums) - 1
        if nums[i] < nums[j]:
            inc = 1
        elif nums[i] > nums[j]:
            inc = -1
        else:
            inc = 0
        for i in range(j):
            if inc == 1 and nums[i] > nums[i + 1]:
                return False
            if inc == 0 and nums[i] != nums[i + 1]:
                return False
            if inc == -1 and nums[i] < nums[i + 1]:
                return False
        return True
