class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq_list = []
        for num, freq in count.items():
            freq_list.append((num, freq))
        
        freq_list.sort(key=lambda x: x[1], reverse=True)

        return [num for num, freq in freq_list[:k]]