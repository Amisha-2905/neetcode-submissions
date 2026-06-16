class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * (2 * n)
        # arr[2*n]=[0]
        for i in range(n):
            arr[i] = nums[i]
            arr[i+n] = nums[i]
        return arr
