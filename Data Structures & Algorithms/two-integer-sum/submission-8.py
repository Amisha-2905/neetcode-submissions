class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])
        arr.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            if arr[l][0] + arr[r][0] == target:
                return [min(arr[l][1], arr[r][1]), max(arr[l][1], arr[r][1])]
            elif arr[l][0] + arr[r][0] < target:
                l += 1
            else:
                r -= 1
        return [arr[l][1], arr[r][1]]
        