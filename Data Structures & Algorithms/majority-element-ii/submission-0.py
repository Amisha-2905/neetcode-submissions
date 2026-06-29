class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        base = len(nums) // 3
        output = []
        for key, value in dic.items():
            if value > base:
                output.append(key)
        
        return output
