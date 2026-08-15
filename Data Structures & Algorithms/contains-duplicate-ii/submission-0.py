class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arr = []
        n = len(nums)
        for i in range(n):
            arr.append([nums[i], i])
        arr.sort()
        for i in range(n - 1):
            if arr[i][0] == arr[i + 1][0]:
                if arr[i][1] - arr[i+1][1] <= k and arr[i + 1][1] - arr[i][1] <= k:
                    return True
        return False