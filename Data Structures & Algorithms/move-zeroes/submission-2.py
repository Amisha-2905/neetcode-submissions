class Solution:
    def findzero(self, nums, i, n):
        while i < n and nums[i] != 0:
            i += 1
        return i

    def findnon(self, nums, j, n):
        while j < n and nums[j] == 0:
            j += 1
        return j

    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = self.findzero(nums, 0, n)
        while i < n:
            j = self.findnon(nums, i + 1, n)
            if j == n:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i = self.findzero(nums, i + 1, n)