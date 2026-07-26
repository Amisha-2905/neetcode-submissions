class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum= [0] * len(nums)
        all_neg = 0
        largest_neg = float('-inf')
        output = nums[0]
        for i in range(len(nums)):
            if nums[i] > 0:
                all_neg += 1
            else:
                largest_neg = max(largest_neg, nums[i])
            if i == 0:
                prefix_sum[i] = nums[0]
            else:
                prefix_sum[i] = nums[i] + prefix_sum[i - 1]
            output = max(output, prefix_sum[ i - 1])
            if prefix_sum[i] < 0:
                if i < 0:
                    output = max(output, prefix_sum[i - 1])
                prefix_sum[i] = 0
            else:
                output = max(output, prefix_sum[i])
        if all_neg == 0:
            print(largest_neg)
            output = largest_neg
        return output