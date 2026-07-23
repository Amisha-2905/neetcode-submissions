class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        left = -1
        right = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if left < 0 or mid < left:
                    left = mid
                    while left >= 0 and nums[left] == target:
                        left -= 1
                    left += 1
                if right < 0 or mid > right:
                    right = mid
                    while right < len(nums) and nums[right] == target:
                        right += 1
                    right -= 1
                l = r + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [left, right]